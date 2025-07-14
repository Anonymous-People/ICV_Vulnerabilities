# Data description

The vulnerability data mentioned in the article can be found in the ICV_study.* file, which contains all the data we have analyzed. The data is available in two formats: CSV and XLSX. If you need to download the dataset, you can choose the format that suits your needs. Note that in the Attack surface column, 1 represents short, 2 represents mid-range, and 3 represents remote.

Besides, we have introduced the attack paths for 14 types of connected vehicle vulnerabilities. The detailed flowcharts are available in the AttackPath folder. Although these contents were not specifically described in the paper due to security concerns, we will introduce the specifics of each attack method in detail through blog posts.

# Vulnerability risk level determination table
In the RISK TAXONOMY section of the paper, we mentioned the Vulnerability Risk Level Determination Table. The original text is as follows:
> To prioritize remediation based on impact severity, we classify vulnerabilities by risk, resulting in 4 risk levels, such as low (L), medium (M), high (H), and critical (C).
> Specifically, we measures the severity of vulnerabilities using two dimensions: the ease of conducting an attack and the impact of the attack.
> A relative scoring system from 1 to 4 is applied, and the risk level is determined based on the **vulnerability risk level determination table**.
> The scoring of each vulnerability is completed through collaboration between experts and the submitter, consisting of three steps: initial scoring by the submitter, expert review, and final consensus, ensuring fairness and accuracy.
> For example, if both the ease of conducting the attack and the impact score 4, the vulnerability is classified as critical.

The specific content of the table is as follows:
|                | Impact level 1 | Impact level 2 | Impact level 3 | Impact level 4 |
|----------------|:--------------:|:--------------:|:--------------:|:--------------:|
| Attack level 1 |      Low       |      Low       |     Medium     |     Medium     |
| Attack level 2 |      Low       |     Medium     |     Medium     |      High      |
| Attack level 3 |     Medium     |     Medium     |      High      |      High      |
| Attack level 4 |     Medium     |      High      |      High      |    Critical    |

The ratings of 1, 2, 3, and 4 are based on strict criteria that have been widely recognized by both vulnerability submitters and ICV experts. 
In fact, these specific guidelines are used to ensure fairness in vulnerability scoring during the competition. 
However, providing these details may compromise anonymity. 
Therefore, we will refrain from elaborating on the specifics during the submission stage.

