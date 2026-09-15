import pandas as pd 
import requests
import matplotlib.pyplot as plt
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

gene = input('Enter gene symbol: ')
search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term={gene}[Gene]+AND+human[Organism]&retmode=json"
response = requests.get(search_url).json()
id_list = response['esearchresult']['idlist']
target_id = id_list[0]
fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={target_id}&rettype=fasta&retmode=text"
raw_fasta = requests.get(fetch_url).text

lines = raw_fasta.strip().split('\n')
header = lines[0]
sequence = "".join(lines[1:]).upper()
seq_len = len(sequence)
g_count = sequence.count('G')
c_count = sequence.count('C')
gc_content = ((g_count + c_count)/seq_len)*100 if seq_len > 0 else 0.0
atg_count = sequence.count('ATG')

df = pd.DataFrame([{
    'gene_symbol': gene,
    'accession_id': target_id,
    'length': seq_len,
    'gc_content': round(gc_content, 2),
    'atg_count': atg_count
}])

plt.style.use('ggplot')
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

bases = ['A', 'T', 'G', 'C']
counts = [sequence.count(b) for b in bases]
axs[0, 0].bar(bases, counts, color=['blue', 'orange', 'green', 'red'])
axs[0, 0].set_title("Nucleotide Frequency")

axs[0, 1].bar(['GC Content', 'AT Content'], [gc_content, 100 - gc_content], color=['purple', 'gray'])
axs[0, 1].set_ylabel("Percentage (%)")
axs[0, 1].set_title("GC/AT Ratio")

axs[1, 0].barh(['Length (bp)'], [seq_len], color='teal')
axs[1, 0].set_title("Total Sequence Size")

axs[1, 1].axis('off')
summary_text = f"Gene: {gene}\nAccession ID: {target_id}\nLength: {seq_len} bp\nGC Content: {gc_content:.2f}%\nStart Codons (ATG): {atg_count}\nVault Status: LOGGED"
axs[1, 1].text(0.1, 0.3, summary_text, fontsize=12, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))
axs[1, 1].set_title("BioInformatix Metadata Card")

plt.tight_layout()
plt.savefig('bioinformatix_summary.png', dpi=300)
plt.show()


conn = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bioinformatix_vault (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gene_symbol VARCHAR(50),
        accession_id VARCHAR(50),
        sequence_length INT,
        gc_content FLOAT,
        atg_count INT,
        logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
 """)  

insert_query = """
    INSERT INTO bioinformatix_vault (gene_symbol, accession_id, sequence_length, gc_content, atg_count)
    VALUES (%s, %s, %s, %s, %s)
"""
values = (
    df['gene_symbol'].iloc[0],
    df['accession_id'].iloc[0],
    int(df['length'].iloc[0]),
    float(df['gc_content'].iloc[0]),
    int(df['atg_count'].iloc[0])
)

cursor.execute(insert_query, values)
conn.commit()
cursor.close()
conn.close()
