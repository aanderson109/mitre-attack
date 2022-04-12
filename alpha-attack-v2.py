from mitreattack import attackToExcel
from stix2 import Filter
from stix2.v21 import AttackPattern
from stix2 import MemoryStore
import requests
import mitreattack.attackToExcel.attackToExcel as aE
import mitreattack.attackToExcel.stixToDf as sD

attackdata = aE.get_stix_data("enterprise-attack")
techniques_data = sD.techniquesToDf(attackdata, "enterprise-attack")

# show t1102 and subtechniques of t1102
techniques_df = techniques_data["techniques"]
print(techniques_df[techniques_df["ID"].str.contains("T1102")]["name"])

# result should be something like this:
# 512                                 Web Service
# 38     Web Service: Bidirectional Communication
# 121             Web Service: Dead Drop Resolver
# 323          Web Service: One-Way Communication
# Name: name, dtype: object

# gets citation
citations_df = techniques_data["citations"]
print(citations_df[citations_df["reference"].str.contains("LOLBAS Wmic")])
#         references                                         citation                                       url
# 1010 LOLBAS Wmic LOLBAS. (n.d.). Wmic.exe. Retrieved July 31, 2.. https://lolbas-project.io/lolbas/Binari...