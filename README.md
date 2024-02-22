## Installiation

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Running

1. Copy the payslip into the project root, make sure it's called ```PaySlip.pdf```, captialisation is important if running on Linux or Mac

2. Run the script passing in the persons initials as the first argument.
   e.g. If you're trying to decrypt John Smiths payslip run:

   ```bash
   $ python decrypt.py js
   ```

Once the script has completed it will have created a decrypted copy of
the ```PaySlip.pdf``` file called ```nopassword.pdf```
