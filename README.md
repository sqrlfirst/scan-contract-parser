# scan-contract-parser
Parser for source code of verified contracts on EVM blockchain explorers.


## STEP 1 

    - open code from webpage and save all into 1 file 
    - get name of main contract, compiler version and other information

## STEP 2 

    - remove deps to other files 
    - check if contract is upgradeable and has implementation -> go to implementation

## STEP 3 

    - check if a dep is common used opensource lib and change source files to it 
    - check if there are connections on other already deployed contracts on chain and list them
