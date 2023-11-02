# Toolbox

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/ndaskalovic/finance-toolbox.git
```
Follow [these](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-token) instructions if you need to generate a private access token (PAC).

## Usage
```python
from toolbox import scrape_bls, format_bls_data
```
## License
[MIT](https://choosealicense.com/licenses/mit/)