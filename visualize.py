import json
import matplotlib.pyplot as plt
import random

percentage_random = 0.02
with open('go-github_raw.json', 'r') as file:
    ext_data = json.load(file)

# Assuming 'ext_data' is the extracted data dictionary
commits = [commit['sha'] for commit in ext_data['commits']]


sample_size = int(percentage_random * len(commits))
selected_commits = random.sample(commits, sample_size)

total_added_lines = []

for commit in ext_data['commits']:
    if 'modified_files' in commit and commit['modified_files']:
        total_added_lines.append(commit['modified_files'][0]['added'])
    else:
        # Handle the case where 'modified_files' is absent or empty
        total_added_lines.append(0)

# Filter the total_added_lines based on the selected_commits
# selected_lines = [total_added_lines[commits.index(commit)] for commit in selected_commits]
# print(total_added_lines[:10])
print(max(total_added_lines))
# plt.figure(figsize=(10, 6))
# plt.boxplot(total_added_lines)
# plt.xlabel('Commits')
# plt.ylabel('Total Added Lines')
# plt.title(f'Total Added Lines per Commit (Random {percentage_random*100}%)')
# # plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

