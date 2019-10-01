# CRyptoCrowd 2.1.0.0

__Mandatory Update__

CRyptoCrowd 2.1.0.0 is a mandatory update to address bugs and introduce enhancements that require a network protocol change.

## Governance
- Modified proposals on testnet to allow for a greater finalization period. 
- Label update for finalized hash budget show status check.
- Fixed issue with old proposals that have been removed causing an error on older finalized budgets, now only last cycle should be shown for `mnfinalbudget` show command
- Change finalization fee for budget proposals from 50 XCRC to 5 XCRC.  This is the fee that is paid by the developers to finalize the proposed budgets. 

## QT/UI
- Add Tor service icon to the status bar that will show during Tor service usage and existing connection to the onion network.
- Added masternode configuration UI that allows for easy adding of masternodes from within the wallet.  Helper features are also existing in the UI to simplify the process as needed automatically.
- Added governance budget and proposal management tab to the wallet.  Now proposals can be created, submitted, and voted on from within the wallet.
- Removed old QT version checks in favor of full support for version 5.7.1+.
- Modified dialog components to hide the help feature of the dialog on Windows.
- Properly set `involvesWatchAddress` in the transaction record. 
- Fixed warning message during first open on the blockchain explorer in the wallet. 
- Corrected some text formatting in the UI and translations.
- Added some missing languages and other i18n cleanups outside the previously stated.
- Replaced UI icons and fixed icon references in the wallet.

## Zerocoin
- Corrected the confirmation information for zXCRC transactions in the transaction list and overview page.
- Lessoned zXCRC confirmation count (UI only) in favor of proper icon referencing. 


## Technical
- Added Docker container support to the core system.
- Modified `setstakesplitthreshold` to act in more natural and anticipated behavior.  Staking XCRC will be split - equally as long as it does not go below the split threshold.  
- Fixes bulwark-crypto#148 provide better handling for unlocking of the wallet when in anonymization and staking only mode checked.  If unlock elevation is requested then the wallet is locked to ensure proper password requirements.
- Implemented new coin staking requirements at the consensus level that will be activated via Spork.  New requirements will ensure that stakes meet the 12hr requirement before being valid for staking.
- Incremented the active node protocol version for the next release.
- Added extra handling to wallet UI in regards to banned peers and updating the banned peer list on change.
- Added warning to console dump commands (dumpprivkey & dumpwallet) and a general warning to console.
- Modified build system configuration to work with latest build tools.
- Use correct COINBASE_MATURITY value in MultiSend.
- Improved logging and print calls.
- Stop using dummy strings in client wallet version information.
- Cleaned up Travis CI build configuration in favor on private build cluster. 

## Miscellaneous
- General documentation cleanup and updates.