2025-10-19 10:49
Initialized repository for CS4348 Project 1. Reviewed both provided PDFs. Outlined project structure: three Python scripts (logger.py, encryptor.py, driver.py), plus devlog.md and README.md. No external libraries, Linux compatibility required. Plan is to start by implementing logger.py. Pushed empty initial files with placeholder docstrings.


2025-10-19 11:12
Finished logger.py. Takes log file destination as argument, reads actions/messages from stdin, writes to log file with YYYY-MM-DD HHMM timestamp. Ending on QUIT line per spec. Manual tests: lines appear in file and timestamp is formatted as required.

2025-10-19 11:44
Completed encryptor.py. Accepts PASS to set key, ENCRYPT/DECRYPT for Vigenère operations, QUIT to exit. Input/output via stdin/stdout. Error handling: enforces password and argument letter-only. Manual tests: encryption/decryption output as expected.


2025-10-19 1:25
Completed driver.py: launches logger and encryption subprocesses, supports interactive user menu, session history, error handling. Also finalized README.md as per assignment. Full system test: all required features and logging confirmed. Ready for packaging and submission.
