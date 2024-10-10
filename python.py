l = [
  {
    "id": "bitcoin",
    "name": "Bitcoin",
    "coinId": 0,
    "symbol": "BTC",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/0'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      },
      {
        "name": "legacy",
        "path": "m/44'/0'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      },
      {
        "name": "testnet",
        "path": "m/84'/1'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 0,
    "p2shPrefix": 5,
    "hrp": "bc",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://mempool.space",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0607f62530b68cfcc91c57a1702841dd399a899d0eecda8e31ecca3f52f01df2",
      "sampleAccount": "17A16QmavnUfCW11DAApiJxp7ARnxN5pGX"
    },
    "info": {
      "url": "https://bitcoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "litecoin",
    "name": "Litecoin",
    "coinId": 2,
    "symbol": "LTC",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/2'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      },
      {
        "name": "legacy",
        "path": "m/44'/2'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 48,
    "p2shPrefix": 50,
    "hrp": "ltc",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockchair.com",
      "txPath": "/litecoin/transaction/",
      "accountPath": "/litecoin/address/"
    },
    "info": {
      "url": "https://litecoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "doge",
    "name": "Dogecoin",
    "coinId": 3,
    "symbol": "DOGE",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/3'/0'/0/0",
        "xpub": "dgub",
        "xprv": "dgpv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 30,
    "p2shPrefix": 22,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockchair.com",
      "txPath": "/dogecoin/transaction/",
      "accountPath": "/dogecoin/address/"
    },
    "info": {
      "url": "https://dogecoin.com",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "dash",
    "name": "Dash",
    "coinId": 5,
    "symbol": "DASH",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/5'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 76,
    "p2shPrefix": 16,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockchair.com",
      "txPath": "/dash/transaction/",
      "accountPath": "/dash/address/"
    },
    "info": {
      "url": "https://dash.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "viacoin",
    "name": "Viacoin",
    "coinId": 14,
    "symbol": "VIA",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/14'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      },
      {
        "name": "legacy",
        "path": "m/44'/14'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 71,
    "p2shPrefix": 33,
    "hrp": "via",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.viacoin.org",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://viacoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "groestlcoin",
    "name": "Groestlcoin",
    "coinId": 17,
    "symbol": "GRS",
    "decimals": 8,
    "blockchain": "Groestlcoin",
    "derivation": [
      {
        "path": "m/84'/17'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 36,
    "p2shPrefix": 5,
    "hrp": "grs",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "groestl512d",
    "explorer": {
      "url": "https://blockchair.com",
      "txPath": "/groestlcoin/transaction/",
      "accountPath": "/groestlcoin/address/"
    },
    "info": {
      "url": "https://www.groestlcoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "digibyte",
    "name": "DigiByte",
    "coinId": 20,
    "symbol": "DGB",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/20'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 30,
    "p2shPrefix": 63,
    "hrp": "dgb",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://digiexplorer.info",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://www.digibyte.io",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "monacoin",
    "name": "Monacoin",
    "coinId": 22,
    "symbol": "MONA",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "legacy",
        "path": "m/44'/22'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      },
      {
        "name": "segwit",
        "path": "m/84'/22'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 50,
    "p2shPrefix": 55,
    "hrp": "mona",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockbook.electrum-mona.org",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://monacoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "decred",
    "name": "Decred",
    "coinId": 42,
    "symbol": "DCR",
    "decimals": 8,
    "blockchain": "Decred",
    "derivation": [
      {
        "path": "m/44'/42'/0'/0/0",
        "xpub": "dpub",
        "xprv": "dprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "staticPrefix": 7,
    "p2pkhPrefix": 63,
    "p2shPrefix": 26,
    "publicKeyHasher": "blake256ripemd",
    "base58Hasher": "blake256d",
    "explorer": {
      "url": "https://dcrdata.decred.org",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://decred.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "syscoin",
    "name": "Syscoin",
    "coinId": 57,
    "symbol": "SYS",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/57'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      },
      {
        "name": "legacy",
        "path": "m/44'/57'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 63,
    "p2shPrefix": 5,
    "hrp": "sys",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://sys1.bcfn.ca",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "19e043f76f6ffc960f5fe93ecec37bc37a58ae7525d7e9cd6ed40f71f0da60eb",
      "sampleAccount": "sys1qh3gvhnzq2ch7w8g04x8zksr2mz7r90x7ksmu40"
    },
    "info": {
      "url": "https://syscoin.org",
      "source": "https://github.com/syscoin",
      "rpc": "https://sys1.bcfn.ca",
      "documentation": "https://docs.syscoin.org"
    }
  },
  {
    "id": "base",
    "name": "Base",
    "coinId": 8453,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "8453",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://basescan.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x4acb15506b7696a2dfac4258f3f86392b4b2b717a3f316a8aa78509b2c3b6ab4",
      "sampleAccount": "0xb8ff877ed78ba520ece21b1de7843a8a57ca47cb"
    },
    "info": {
      "url": "https://base.mirror.xyz/",
      "source": "https://github.com/base-org",
      "rpc": "https://mainnet.base.org",
      "documentation": "https://docs.base.org/"
    }
  },
  {
    "id": "linea",
    "name": "Linea",
    "coinId": 59144,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "59144",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://lineascan.build",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x0c7086f96865f4fcad58d7f3449db7baab9fce2625bcb79e7ea26676aa0d3420",
      "sampleAccount": "0xbf71018f716ca6c64b0b12622f87a26b3b86100f"
    },
    "info": {
      "url": "https://linea.build",
      "source": "https://github.com/LineaLabs",
      "rpc": "https://rpc.linea.build",
      "documentation": "https://docs.linea.build"
    }
  },
  {
    "id": "mantle",
    "name": "Mantle",
    "coinId": 5000,
    "symbol": "MNT",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "5000",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.mantle.xyz",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xfae996ea23f1ff9909ac04d26ae6e52ab600a84163fab9e0e893483c685629dd",
      "sampleAccount": "0xA295EEFd401C8BE1457F266d3e73cdD015e5CFbb"
    },
    "info": {
      "url": "https://www.mantle.xyz",
      "source": "https://github.com/mantlenetworkio",
      "rpc": "https://rpc.mantle.xyz",
      "documentation": "https://docs.mantle.xyz/network/introduction/overview"
    }
  },
  {
    "id": "zeneon",
    "name": "Zen EON",
    "coinId": 7332,
    "symbol": "ZEN",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "7332",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://eon-explorer.horizenlabs.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xb462e3dac8eef21957d3b6cff3c184d083434367a726dd871e98a774f4d037a5",
      "sampleAccount": "0x09bCfC348101B1179BCF3837aC996cF09357215f"
    },
    "info": {
      "url": "https://eon.horizen.io",
      "source": "https://github.com/HorizenOfficial/eon",
      "rpc": "https://eon-rpc.horizenlabs.io/ethv1",
      "documentation": "https://eon.horizen.io/docs"
    }
  },
  {
    "id": "ethereum",
    "name": "Ethereum",
    "coinId": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://etherscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x9edaf0f7d9c6629c31bbf0471fc07d696c73b566b93783f7e25d8d5d2b62fa4f",
      "sampleAccount": "0x5bb497e8d9fe26e92dd1be01e32076c8e024d167"
    },
    "info": {
      "url": "https://ethereum.org",
      "source": "https://github.com/ethereum/go-ethereum",
      "rpc": "https://mainnet.infura.io",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "classic",
    "name": "Ethereum Classic",
    "coinId": 61,
    "symbol": "ETC",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/61'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "61",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blockscout.com/etc/mainnet",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x66004165d3901819dc22e568931591d2e4287bda54995f4ce2701a12016f5997",
      "sampleAccount": "0x9eab4b0fc468a7f5d46228bf5a76cb52370d068d"
    },
    "info": {
      "url": "https://ethereumclassic.org",
      "source": "https://github.com/ethereumclassic/go-ethereum",
      "rpc": "https://www.ethercluster.com/etc",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "icon",
    "name": "ICON",
    "coinId": 74,
    "symbol": "ICX",
    "decimals": 18,
    "blockchain": "Icon",
    "derivation": [
      {
        "path": "m/44'/74'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://tracker.icon.foundation",
      "txPath": "/transaction/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://icon.foundation",
      "source": "https://github.com/icon-project/icon-rpc-server",
      "rpc": "http://ctz.icxstation.com:9000/api/v3",
      "documentation": "https://www.icondev.io/docs/icon-json-rpc-v3"
    }
  },
  {
    "id": "verge",
    "name": "Verge",
    "coinId": 77,
    "symbol": "XVG",
    "decimals": 6,
    "blockchain": "Verge",
    "derivation": [
      {
        "path": "m/84'/77'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 30,
    "p2shPrefix": 33,
    "hrp": "vg",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://verge-blockchain.info",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "8c99979a2b25a46659bff35b238aab1c3158f736f215d99526429c7c96203581",
      "sampleAccount": "DFre88gd87bAZQdnS7dbBLwT6GWiGFMQB6"
    },
    "info": {
      "url": "https://vergecurrency.com",
      "source": "https://github.com/vergecurrency/verge",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "pivx",
    "name": "Pivx",
    "coinId": 119,
    "symbol": "PIVX",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/119'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 30,
    "p2shPrefix": 13,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://pivx.ccore.online",
      "txPath": "/transaction/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://pivx.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "zen",
    "name": "Zen",
    "coinId": 121,
    "symbol": "ZEN",
    "decimals": 8,
    "blockchain": "Zen",
    "derivation": [
      {
        "path": "m/44'/121'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "staticPrefix": 32,
    "p2pkhPrefix": 137,
    "p2shPrefix": 150,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.horizen.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "b7f548640766fb024247accf4e01bec37d88d49c4900357edc84d49a09ff4430",
      "sampleAccount": "znRchPtvEyJJUwGbCALqyjwHJb1Gx6z4H4j"
    },
    "info": {
      "url": "https://www.horizen.io",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "aptos",
    "name": "Aptos",
    "displayName": "Aptos",
    "coinId": 637,
    "symbol": "APT",
    "decimals": 8,
    "chainId": "1",
    "blockchain": "Aptos",
    "derivation": [
      {
        "path": "m/44'/637'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://explorer.aptoslabs.com",
      "txPath": "/txn/",
      "accountPath": "/account/",
      "sampleTx": "0xedc88058e27f6c065fd6607e262cb2a83a65f74301df90c61923014c59f9d465",
      "sampleAccount": "0x60ad80e8cdadb81399e8a738014bc9ec865cef842f7c2cf7d84fbf7e40d065"
    },
    "info": {
      "url": "https://aptoslabs.com/",
      "source": "https://github.com/aptos-labs/aptos-core",
      "rpc": "https://fullnode.mainnet.aptoslabs.com/v1",
      "documentation": "https://fullnode.mainnet.aptoslabs.com/v1/spec#/"
    }
  },
  {
    "id": "sui",
    "name": "Sui",
    "coinId": 784,
    "symbol": "SUI",
    "decimals": 9,
    "blockchain": "Sui",
    "derivation": [
      {
        "path": "m/44'/784'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://explorer.sui.io/",
      "txPath": "/txblock/",
      "accountPath": "/address/",
      "sampleTx": "5i8fbSL6r8yw2xcKmXxwkzHu3wpiyMLsyf2htCvDH8Ao",
      "sampleAccount": "0x259ff8074ab425cbb489f236e18e08f03f1a7856bdf7c7a2877bd64f738b5015"
    },
    "info": {
      "url": "https://sui.io/",
      "source": "https://github.com/MystenLabs/sui",
      "rpc": "https://fullnode.testnet.sui.io",
      "documentation": "https://docs.sui.io/"
    }
  },
  {
    "id": "cosmos",
    "name": "Cosmos",
    "displayName": "Cosmos Hub",
    "coinId": 118,
    "symbol": "ATOM",
    "decimals": 6,
    "chainId": "cosmoshub-4",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "cosmos",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://mintscan.io/cosmos",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "541FA06FB37AC1BF61922143783DD76FECA361830F9876D0342536EE8A87A790",
      "sampleAccount": "cosmos1gu6y2a0ffteesyeyeesk23082c6998xyzmt9mz"
    },
    "info": {
      "url": "https://cosmos.network",
      "source": "https://github.com/cosmos/cosmos-sdk",
      "rpc": "https://stargate.cosmos.network",
      "documentation": "https://cosmos.network/rpc"
    }
  },
  {
    "id": "stargaze",
    "name": "Stargaze",
    "displayName": "Stargaze",
    "coinId": 20000118,
    "symbol": "STARS",
    "decimals": 6,
    "chainId": "stargaze-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "stars",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/stargaze",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://www.stargaze.zone/",
      "source": "https://github.com/public-awesome/stargaze",
      "rpc": "https://stargaze-rpc.polkachu.com/",
      "documentation": "https://docs.stargaze.zone/guides/readme"
    }
  },
  {
    "id": "juno",
    "name": "Juno",
    "displayName": "Juno",
    "coinId": 30000118,
    "symbol": "JUNO",
    "decimals": 6,
    "chainId": "juno-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "juno",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/juno",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://www.junonetwork.io/",
      "source": "https://github.com/CosmosContracts/juno",
      "rpc": "https://juno-rpc.polkachu.com",
      "documentation": "https://docs.junonetwork.io/juno/readme"
    }
  },
  {
    "id": "stride",
    "name": "Stride",
    "displayName": "Stride",
    "coinId": 40000118,
    "symbol": "STRD",
    "decimals": 6,
    "chainId": "stride-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "stride",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/stride",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://stride.zone/",
      "source": "https://github.com/Stride-Labs/stride",
      "rpc": "https://stride-rpc.polkachu.com/",
      "documentation": "https://docs.stride.zone/docs"
    }
  },
  {
    "id": "axelar",
    "name": "Axelar",
    "displayName": "Axelar",
    "coinId": 50000118,
    "symbol": "AXL",
    "decimals": 6,
    "chainId": "axelar-dojo-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "axelar",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/axelar",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://axelar.network/",
      "source": "https://github.com/axelarnetwork/axelar-core",
      "rpc": "https://axelar-rpc.polkachu.com",
      "documentation": "https://docs.axelar.dev/"
    }
  },
  {
    "id": "crescent",
    "name": "Crescent",
    "displayName": "Crescent",
    "coinId": 60000118,
    "symbol": "CRE",
    "decimals": 6,
    "chainId": "crescent-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "cre",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/crescent",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://crescent.network/",
      "source": "https://github.com/crescent-network/crescent",
      "rpc": "https://crescent-rpc.polkachu.com",
      "documentation": "https://docs.crescent.network/introduction/what-is-crescent"
    }
  },
  {
    "id": "kujira",
    "name": "Kujira",
    "displayName": "Kujira",
    "coinId": 70000118,
    "symbol": "KUJI",
    "decimals": 6,
    "chainId": "kaiyo-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "kujira",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/kujira",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://kujira.app/",
      "source": "https://github.com/Team-Kujira/core",
      "rpc": "https://kujira-rpc.polkachu.com",
      "documentation": "https://docs.kujira.app/introduction/readme"
    }
  },
  {
    "id": "comdex",
    "name": "Comdex",
    "displayName": "Comdex",
    "coinId": 80000118,
    "symbol": "CMDX",
    "decimals": 6,
    "chainId": "comdex-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "comdex",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/comdex",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "04C790D09A40EE958DBDD385B679B5EB60C10F9BC1389CC8F896DC9193A5ED6C",
      "sampleAccount": "comdex1jz7av7cq45gh5hhrugtak7lkps2ga5v0u64nz6"
    },
    "info": {
      "url": "https://comdex.one/",
      "documentation": "https://docs.comdex.one/"
    }
  },
  {
    "id": "neutron",
    "name": "Neutron",
    "displayName": "Neutron",
    "coinId": 90000118,
    "symbol": "NTRN",
    "decimals": 6,
    "chainId": "neutron-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "neutron",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/neutron",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "E18BA087009A05EB6A15A22FE30BA99379B909F74A74120E6F92B9882C45F0D7",
      "sampleAccount": "neutron1pm4af8pcurxssdxztqw9rexx5f8zfq7uzqfmy8"
    },
    "info": {
      "url": "https://neutron.org/",
      "documentation": "https://docs.neutron.org/"
    }
  },
  {
    "id": "sommelier",
    "name": "Sommelier",
    "displayName": "Sommelier",
    "coinId": 11000118,
    "symbol": "SOMM",
    "decimals": 6,
    "chainId": "sommelier-3",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "somm",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/sommelier",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "E73A9E5E534777DDADF7F69A5CB41972894B862D1763FA4081FE913D8D3A5E80",
      "sampleAccount": "somm10d5wmqvezwtj20u5hg3wuvwucce2nhsy0tzqgn"
    },
    "info": {
      "url": "https://www.sommelier.finance/"
    }
  },
  {
    "id": "fetchai",
    "name": "FetchAI",
    "displayName": "Fetch AI",
    "coinId": 12000118,
    "symbol": "FET",
    "decimals": 6,
    "chainId": "fetchhub-4",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "fetch",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/fetchai",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "7EB4F6C26809BA047F81CEFD0889775AC8522B7B8AF559B436083BE7039C5EA6",
      "sampleAccount": "fetch1t3qet68dr0qkmrjtq89lrx837qa2t05265qy6s"
    },
    "info": {
      "url": "https://fetch.ai/",
      "documentation": "https://docs.fetch.ai/"
    }
  },
  {
    "id": "mars",
    "name": "Mars",
    "displayName": "Mars Hub",
    "coinId": 13000118,
    "symbol": "MARS",
    "decimals": 6,
    "chainId": "mars-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "mars",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/mars-protocol",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "C12120760C71189A678739E0F1FD4EFAF2C29EA660B57A359AC728F89FAA7528",
      "sampleAccount": "mars1nnjy6nct405pzfaqjm3dsyw0pf0kyw72vhw4pr"
    },
    "info": {
      "url": "https://marsprotocol.io/",
      "documentation": "https://docs.marsprotocol.io/"
    }
  },
  {
    "id": "umee",
    "name": "Umee",
    "displayName": "Umee",
    "coinId": 14000118,
    "symbol": "UMEE",
    "decimals": 6,
    "chainId": "umee-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "umee",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/umee",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "65B4B52C5F324F2287540847A114F645D89D544D99F793879FB3DBFF2CFEFC84",
      "sampleAccount": "umee16934q0qf4akw8qruy5y8v748rvtxxjckgsecq4"
    },
    "info": {
      "url": "https://umee.cc/",
      "documentation": "https://umeeversity.umee.cc/developers/"
    }
  },
  {
    "id": "noble",
    "name": "Noble",
    "displayName": "Noble",
    "coinId": 18000118,
    "symbol": "USDC",
    "decimals": 6,
    "chainId": "noble-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "noble",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/noble",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "EA231079975A058FEC28EF372B445763918C098DE033E868E2E035F3F98C59C7",
      "sampleAccount": "noble1y2egevq0nyzm7w6a9kpxkw86eqytcvxpwsp6d9"
    },
    "info": {
      "url": "https://nobleassets.xyz/"
    }
  },
  {
    "id": "sei",
    "name": "Sei",
    "displayName": "Sei",
    "coinId": 19000118,
    "symbol": "SEI",
    "decimals": 6,
    "blockchain": "Cosmos",
    "chainId": "pacific-1",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "sei",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/sei",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "4A2114EE45317439690F3BEA9C8B6CFA11D42CF978F9487754902D372EEB488C",
      "sampleAccount": "sei155hqv2rsypqzq0zpjn72frsxx4l6tcmplw63m2"
    },
    "info": {
      "url": "https://sei.io/",
      "documentation": "https://docs.sei.io/"
    }
  },
  {
    "id": "tia",
    "name": "Tia",
    "displayName": "Celestia",
    "coinId": 21000118,
    "symbol": "TIA",
    "decimals": 6,
    "blockchain": "Cosmos",
    "chainId": "celestia",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "celestia",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/celestia",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "FF370C65D8D67B8236F9D3A8D2B1256337C60C1965092CADD1FA970288FCE99B",
      "sampleAccount": "celestia1tt4tv4jrs4twdtzwywxd8u65duxgk8y73wvfu2"
    },
    "info": {
      "url": "https://celestia.org/",
      "documentation": "https://docs.celestia.org/"
    }
  },
  {
    "id": "coreum",
    "name": "Coreum",
    "displayName": "Coreum",
    "coinId": 10000990,
    "symbol": "CORE",
    "decimals": 6,
    "chainId": "coreum-mainnet-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/990'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "core",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/coreum",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "32A4AE2AE6AAE31E75EDDADE0AB9F1499ABD5AD8D3F261ADEF2805CD46FF74E7",
      "sampleAccount": "core1zmwdnfpwuymwn0fkwnj2aaje34npd5sqgjxq9v"
    },
    "info": {
      "url": "https://www.coreum.com/",
      "documentation": "https://www.coreum.com/developers"
    }
  },
  {
    "id": "quasar",
    "name": "Quasar",
    "displayName": "Quasar",
    "coinId": 15000118,
    "symbol": "QSR",
    "decimals": 6,
    "chainId": "quasar-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "quasar",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/quasar",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "2898B89C98FE1E8CF1E05A37E4EE5EE5ED83FD957B0CAEE53DE39FC82BF1A033",
      "sampleAccount": "quasar1cqu6w425slheul3jsmyt6q0ec0rs0w0ugkst3k"
    },
    "info": {
      "url": "https://www.quasar.fi/",
      "documentation": "https://docs.quasar.fi/"
    }
  },
  {
    "id": "persistence",
    "name": "Persistence",
    "displayName": "Persistence",
    "coinId": 16000118,
    "symbol": "XPRT",
    "decimals": 6,
    "chainId": "core-1",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "persistence",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/persistence",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "BBD9DEE03A8D7538D8E7398217467F4A2B5690D15773E8A6442E6AEEEFA21E64",
      "sampleAccount": "persistence10ys69560pqr6zmqam80g8s0smtjw6p3ugzmy3u"
    },
    "info": {
      "url": "https://persistence.one/",
      "documentation": "https://docs.persistence.one/"
    }
  },
  {
    "id": "akash",
    "name": "Akash",
    "displayName": "Akash",
    "coinId": 17000118,
    "symbol": "AKT",
    "decimals": 6,
    "chainId": "akashnet-2",
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "akash",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/akash",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "C0083856344425908D5333D4325E3E0DE9D697BA568C6D99C34303819F615D25",
      "sampleAccount": "akash1f4nskxfw8ufhwnajh7xwt0wmdtxm02vwta6krg"
    },
    "info": {
      "url": "https://akash.network/",
      "documentation": "https://docs.akash.network/"
    }
  },
  {
    "id": "zcash",
    "name": "Zcash",
    "coinId": 133,
    "symbol": "ZEC",
    "decimals": 8,
    "blockchain": "Zcash",
    "derivation": [
      {
        "path": "m/44'/133'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "staticPrefix": 28,
    "p2pkhPrefix": 184,
    "p2shPrefix": 189,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockchair.com/zcash",
      "txPath": "/transaction/",
      "accountPath": "/address/",
      "sampleTx": "f2438a93039faf08d39bd3df1f7b5f19a2c29ffe8753127e2956ab4461adab35",
      "sampleAccount": "t1Yfrf1dssDLmaMBsq2LFKWPbS5vH3nGpa2"
    },
    "info": {
      "url": "https://z.cash",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "firo",
    "name": "Firo",
    "coinId": 136,
    "symbol": "FIRO",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/136'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 82,
    "p2shPrefix": 7,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.firo.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "09a60d58b3d17519a42a8eca60750c33b710ca8f3ca71994192e05c248a2a111",
      "sampleAccount": "a8ULhhDgfdSiXJhSZVdhb8EuDc6R3ogsaM"
    },
    "info": {
      "url": "https://firo.org/",
      "source": "https://github.com/firoorg/firo",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "komodo",
    "name": "Komodo",
    "coinId": 141,
    "symbol": "KMD",
    "decimals": 8,
    "blockchain": "Zcash",
    "derivation": [
      {
        "path": "m/44'/141'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 60,
    "p2shPrefix": 85,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://kmdexplorer.io/",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "f53bd1a5c0f5dc4b60ba9a1882742ea96faa996e1b870795812a29604dd7829e",
      "sampleAccount": "RWvfkt8UjbPWXgeZEcgYmKw2vA1bbAx5t2"
    },
    "info": {
      "url": "https://komodoplatform.com",
      "source": "https://github.com/KomodoPlatform/komodo",
      "rpc": "",
      "documentation": "https://developers.komodoplatform.com"
    }
  },
  {
    "id": "ripple",
    "name": "XRP",
    "coinId": 144,
    "symbol": "XRP",
    "decimals": 6,
    "blockchain": "Ripple",
    "derivation": [
      {
        "path": "m/44'/144'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "explorer": {
      "url": "https://bithomp.com",
      "txPath": "/explorer/",
      "accountPath": "/explorer/",
      "sampleTx": "E26AB8F3372D2FC02DEC1FD5674ADAB762D684BFFDBBDF5D674E9D7CF4A47054",
      "sampleAccount": "rfkH7EuS1XcSkB9pocy1R6T8F4CsNYixYU"
    },
    "info": {
      "url": "https://ripple.com/xrp",
      "source": "https://github.com/ripple/rippled",
      "rpc": "https://s2.ripple.com:51234",
      "documentation": "https://xrpl.org/rippled-api.html"
    }
  },
  {
    "id": "bitcoincash",
    "name": "Bitcoin Cash",
    "coinId": 145,
    "symbol": "BCH",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/145'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 0,
    "p2shPrefix": 5,
    "hrp": "bitcoincash",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockchair.com",
      "txPath": "/bitcoin-cash/transaction/",
      "accountPath": "/bitcoin-cash/address/"
    },
    "info": {
      "url": "https://bitcoincash.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "stellar",
    "name": "Stellar",
    "coinId": 148,
    "symbol": "XLM",
    "decimals": 7,
    "blockchain": "Stellar",
    "derivation": [
      {
        "path": "m/44'/148'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://blockchair.com/stellar",
      "txPath": "/transaction/",
      "accountPath": "/account/",
      "sampleTx": "8a7ff7261e8b3f31af7f6ed257c2e9fe7c47afcd9b1ce1be1bfc1bc5f6a3ad9e",
      "sampleAccount": "GCILJZQ3CKBKBUJWW4TAM6Q37LJA5MQX6GMSFSQN75BPLWIZ33OPRG52"
    },
    "info": {
      "url": "https://stellar.org",
      "source": "https://github.com/stellar/go",
      "rpc": "https://horizon.stellar.org",
      "documentation": "https://www.stellar.org/developers/horizon/reference"
    }
  },
  {
    "id": "bitcoingold",
    "name": "Bitcoin Gold",
    "coinId": 156,
    "symbol": "BTG",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/84'/156'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      },
      {
        "name": "legacy",
        "path": "m/44'/156'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 38,
    "p2shPrefix": 23,
    "hrp": "btg",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.bitcoingold.org/insight",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "2f807d7734de35d2236a1b3d8704eb12954f5f82ea66987949b10e94d9999b23",
      "sampleAccount": "GJjz2Du9BoJQ3CPcoyVTHUJZSj62i1693U"
    },
    "info": {
      "url": "https://bitcoingold.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "nano",
    "name": "Nano",
    "coinId": 165,
    "symbol": "XNO",
    "decimals": 30,
    "blockchain": "Nano",
    "derivation": [
      {
        "path": "m/44'/165'/0'"
      }
    ],
    "curve": "ed25519Blake2bNano",
    "publicKeyType": "ed25519Blake2b",
    "url": "https://nano.org",
    "explorer": {
      "url": "https://www.nanolooker.com",
      "txPath": "/block/",
      "accountPath": "/account/",
      "sampleTx": "C264DB7BF40738F0CEFF19B606746CB925B713E4B8699A055699E0DC8ABBC70F",
      "sampleAccount": "nano_1wpj616kwhe1y38y1mspd8aub8i334cwybqco511iyuxm55zx8d67ptf1tsf"
    },
    "info": {
      "url": "https://nano.org",
      "source": "https://github.com/nanocurrency/nano-node",
      "rpc": "",
      "documentation": "https://docs.nano.org/commands/rpc-protocol/"
    }
  },
  {
    "id": "ravencoin",
    "name": "Ravencoin",
    "coinId": 175,
    "symbol": "RVN",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/175'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 60,
    "p2shPrefix": 122,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://blockbook.ravencoin.org",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://ravencoin.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "poa",
    "name": "POA Network",
    "coinId": 178,
    "symbol": "POA",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/178'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "99",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blockscout.com",
      "txPath": "/poa/core/tx/",
      "accountPath": "/poa/core/address/"
    },
    "info": {
      "url": "https://poa.network",
      "source": "https://github.com/poanetwork/parity-ethereum",
      "rpc": "https://core.poa.network",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "eos",
    "name": "EOS",
    "coinId": 194,
    "symbol": "EOS",
    "decimals": 4,
    "blockchain": "EOS",
    "derivation": [
      {
        "path": "m/44'/194'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "explorer": {
      "url": "https://bloks.io",
      "txPath": "/transaction/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "http://eos.io",
      "source": "https://github.com/eosio/eos",
      "rpc": "",
      "documentation": "https://developers.eos.io/eosio-nodeos/reference"
    }
  },
  {
    "id": "wax",
    "name": "WAX",
    "coinId": 14001,
    "symbol": "WAXP",
    "decimals": 4,
    "blockchain": "EOS",
    "derivation": [
      {
        "path": "m/44'/194'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "explorer": {
      "url": "https://wax.bloks.io",
      "txPath": "/transaction/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "http://wax.io",
      "source": "https://github.com/worldwide-asset-exchange/wax-blockchain",
      "rpc": "https://wax.blacklusion.io",
      "documentation": "https://https://developer.wax.io"
    }
  },
  {
    "id": "tron",
    "name": "Tron",
    "coinId": 195,
    "symbol": "TRX",
    "decimals": 6,
    "blockchain": "Tron",
    "derivation": [
      {
        "path": "m/44'/195'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://tronscan.org",
      "txPath": "/#/transaction/",
      "accountPath": "/#/address/"
    },
    "info": {
      "url": "https://tron.network",
      "source": "https://github.com/tronprotocol/java-tron",
      "rpc": "https://api.trongrid.io",
      "documentation": "https://developers.tron.network/docs/tron-wallet-rpc-api"
    }
  },
  {
    "id": "fio",
    "name": "FIO",
    "coinId": 235,
    "symbol": "FIO",
    "decimals": 9,
    "blockchain": "FIO",
    "derivation": [
      {
        "path": "m/44'/235'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "url": "https://fioprotocol.io/",
    "explorer": {
      "url": "https://explorer.fioprotocol.io",
      "txPath": "/transaction/",
      "accountPath": "/account/",
      "sampleTx": "930d1d3cf8988b39b5f64b64e9d61314a3e05a155d9e3505bdf863aab1adddf3",
      "sampleAccount": "f5axfpgffiqz"
    },
    "info": {
      "url": "https://fioprotocol.io",
      "source": "https://github.com/fioprotocol/fio",
      "rpc": "https://mainnet.fioprotocol.io",
      "documentation": "https://developers.fioprotocol.io"
    }
  },
  {
    "id": "nimiq",
    "name": "Nimiq",
    "coinId": 242,
    "symbol": "NIM",
    "decimals": 5,
    "blockchain": "Nimiq",
    "derivation": [
      {
        "path": "m/44'/242'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://nimiq.watch",
      "txPath": "/#",
      "accountPath": "/#"
    },
    "info": {
      "url": "https://nimiq.com",
      "source": "https://github.com/nimiq/core-rs",
      "rpc": "",
      "documentation": "https://github.com/nimiq/core-js/wiki/JSON-RPC-API"
    }
  },
  {
    "id": "algorand",
    "name": "Algorand",
    "coinId": 283,
    "symbol": "ALGO",
    "decimals": 6,
    "blockchain": "Algorand",
    "derivation": [
      {
        "path": "m/44'/283'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://app.dappflow.org/explorer",
      "txPath": "/transaction/",
      "accountPath": "/account/",
      "sampleTx": "CR7POXFTYDLC7TV3IXHA7AZKWABUJC52BACLHJQNXAKZJGRPQY3A",
      "sampleAccount": "J4AEINCSSLDA7LNBNWM4ZXFCTLTOZT5LG3F5BLMFPJYGFWVCMU37EZI2AM"
    },
    "info": {
      "url": "https://www.algorand.com/",
      "source": "https://github.com/algorand/go-algorand",
      "rpc": "https://indexer.algorand.network",
      "documentation": "https://developer.algorand.org/docs/algod-rest-paths"
    }
  },
  {
    "id": "iotex",
    "name": "IoTeX",
    "coinId": 304,
    "symbol": "IOTX",
    "decimals": 18,
    "blockchain": "IoTeX",
    "derivation": [
      {
        "path": "m/44'/304'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "io",
    "explorer": {
      "url": "https://iotexscan.io",
      "txPath": "/action/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://iotex.io",
      "source": "https://github.com/iotexproject/iotex-core",
      "rpc": "",
      "documentation": "https://docs.iotex.io/#api"
    }
  },
  {
    "id": "iotexevm",
    "name": "IoTeX EVM",
    "displayName": "IoTeX EVM",
    "coinId": 10004689,
    "symbol": "IOTX",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/304'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "4689",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://iotexscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://iotex.io/",
      "documentation": "https://iotex.io/developers"
    }
  },
  {
    "id": "nervos",
    "name": "Nervos",
    "coinId": 309,
    "symbol": "CKB",
    "decimals": 8,
    "blockchain": "Nervos",
    "derivation": [
      {
        "path": "m/44'/309'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "ckb",
    "explorer": {
      "url": "https://explorer.nervos.org",
      "txPath": "/transaction/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://nervos.org",
      "source": "https://github.com/nervosnetwork/ckb",
      "rpc": "https://mainnet.ckb.dev/rpc",
      "documentation": "https://github.com/nervosnetwork/rfcs"
    }
  },
  {
    "id": "zilliqa",
    "name": "Zilliqa",
    "coinId": 313,
    "symbol": "ZIL",
    "decimals": 12,
    "blockchain": "Zilliqa",
    "derivation": [
      {
        "path": "m/44'/313'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "zil",
    "explorer": {
      "url": "https://viewblock.io",
      "txPath": "/zilliqa/tx/",
      "accountPath": "/zilliqa/address/"
    },
    "info": {
      "url": "https://zilliqa.com",
      "source": "https://github.com/Zilliqa/Zilliqa",
      "rpc": "https://api.zilliqa.com",
      "documentation": "https://apidocs.zilliqa.com"
    }
  },
  {
    "id": "terra",
    "name": "Terra",
    "displayName": "Terra Classic",
    "coinId": 330,
    "symbol": "LUNC",
    "decimals": 6,
    "blockchain": "Cosmos",
    "chainId": "columbus-5",
    "derivation": [
      {
        "path": "m/44'/330'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "terra",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://finder.terra.money/classic",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://terra.money",
      "source": "https://github.com/terra-project/core",
      "rpc": "https://columbus-fcd.terra.dev",
      "documentation": "https://docs.terra.money"
    }
  },
  {
    "id": "terrav2",
    "name": "TerraV2",
    "displayName": "Terra",
    "coinId": 10000330,
    "symbol": "LUNA",
    "decimals": 6,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/330'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "terra",
    "chainId": "phoenix-1",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://finder.terra.money/mainnet",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://terra.money",
      "source": "https://github.com/terra-project/core",
      "rpc": "https://phoenix-lcd.terra.dev",
      "documentation": "https://docs.terra.money"
    }
  },
  {
    "id": "polkadot",
    "name": "Polkadot",
    "coinId": 354,
    "symbol": "DOT",
    "decimals": 10,
    "blockchain": "Polkadot",
    "derivation": [
      {
        "path": "m/44'/354'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "addressHasher": "keccak256",
    "ss58Prefix": 0,
    "explorer": {
      "url": "https://polkadot.subscan.io",
      "txPath": "/extrinsic/",
      "accountPath": "/account/",
      "sampleTx": "0xb96f97d8ee508f420e606e1a6dcc74b88844713ddec2bd7cf4e3aa6b1d6beef4",
      "sampleAccount": "13hJFqnkqQbmgnGQteGntjMjTdmTBRE8Z93JqxsrpgT7Yjd2"
    },
    "info": {
      "url": "https://polkadot.network/",
      "source": "https://github.com/paritytech/polkadot",
      "rpc": "",
      "documentation": "https://polkadot.js.org/api/substrate/rpc.html"
    }
  },
  {
    "id": "everscale",
    "name": "Everscale",
    "coinId": 396,
    "symbol": "EVER",
    "decimals": 9,
    "blockchain": "Everscale",
    "derivation": [
      {
        "path": "m/44'/396'/0'/0/0"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://everscan.io",
      "txPath": "/transactions/",
      "accountPath": "/accounts/",
      "sampleTx": "781238b2b0d15cd4cd2e2a0a142753750cd5e1b2c8b506fcede75a90e02f1268",
      "sampleAccount": "0:d2bf59964a05dee84a0dd1ddc0ad83ba44d49719cf843d689dc8b726d0fb59d8"
    },
    "info": {
      "url": "https://everscale.network/",
      "source": "https://github.com/tonlabs/evernode-ds",
      "rpc": "https://evercloud.dev",
      "documentation": "https://docs.everos.dev/evernode-platform/products/evercloud/get-started"
    }
  },
  {
    "id": "near",
    "name": "NEAR",
    "coinId": 397,
    "symbol": "NEAR",
    "decimals": 24,
    "blockchain": "NEAR",
    "derivation": [
      {
        "path": "m/44'/397'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://nearblocks.io",
      "txPath": "/txns/",
      "accountPath": "/address/",
      "sampleTx": "FPQAMaVnvFHNwNBJWnTttXfdJhp5FvMGGDJEesB8gvbL",
      "sampleAccount": "test-trust.vlad.near"
    },
    "info": {
      "url": "https://nearprotocol.com",
      "source": "https://github.com/nearprotocol/nearcore",
      "rpc": "https://rpc.nearprotocol.com",
      "documentation": "https://docs.nearprotocol.com"
    }
  },
  {
    "id": "aion",
    "name": "Aion",
    "coinId": 425,
    "symbol": "AION",
    "decimals": 18,
    "blockchain": "Aion",
    "derivation": [
      {
        "path": "m/44'/425'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://mainnet.aion.network",
      "txPath": "/#/transaction/",
      "accountPath": "/#/account/"
    },
    "info": {
      "url": "https://aion.network",
      "source": "https://github.com/aionnetwork/aion",
      "rpc": "",
      "documentation": "https://github.com/aionnetwork/aion/wiki/JSON-RPC-API-Docs"
    }
  },
  {
    "id": "kusama",
    "name": "Kusama",
    "coinId": 434,
    "symbol": "KSM",
    "decimals": 12,
    "blockchain": "Kusama",
    "derivation": [
      {
        "path": "m/44'/434'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "addressHasher": "keccak256",
    "ss58Prefix": 2,
    "explorer": {
      "url": "https://kusama.subscan.io",
      "txPath": "/extrinsic/",
      "accountPath": "/account/",
      "sampleTx": "0xcbe0c2e2851c1245bedaae4d52f06eaa6b4784b786bea2f0bff11af7715973dd",
      "sampleAccount": "DbCNECPna3k6MXFWWNZa5jGsuWycqEE6zcUxZYkxhVofrFk"
    },
    "info": {
      "url": "https://kusama.network",
      "source": "https://github.com/paritytech/polkadot",
      "rpc": "wss://kusama-rpc.polkadot.io/",
      "documentation": "https://polkadot.js.org/api/substrate/rpc.html"
    }
  },
  {
    "id": "acala",
    "name": "Acala",
    "coinId": 787,
    "symbol": "ACA",
    "decimals": 12,
    "blockchain": "Polkadot",
    "derivation": [
      {
        "path": "m/44'/787'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "addressHasher": "keccak256",
    "ss58Prefix": 10,
    "explorer": {
      "url": "https://acala.subscan.io",
      "txPath": "/extrinsic/",
      "accountPath": "/account/",
      "sampleTx": "0xf3d58aafb1208bc09d10ba74bbf1c7811dc55a9149c1505256b6fb5603f5047f",
      "sampleAccount": "26JqMKx4HJJcmb1kXo24HYYobiK2jURGCq6zuEzFBK3hQ9Ti"
    },
    "info": {
      "url": "https://acala.network",
      "source": "https://github.com/AcalaNetwork/Acala",
      "rpc": "wss://acala-rpc.dwellir.com",
      "documentation": "https://polkadot.js.org/api/substrate/rpc.html"
    }
  },
  {
    "id": "acalaevm",
    "name": "Acala EVM",
    "coinId": 10000787,
    "slip44": 60,
    "symbol": "ACA",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "787",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blockscout.acala.network",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x4b0b151dd71ed8ef3174da18565790bf14f0a903a13e4f3266c7848bc8841593",
      "sampleAccount": "0x9d1d97aDFcd324Bbd603D3872BD78e04098510b1"
    },
    "info": {
      "url": "https://acala.network",
      "source": "https://github.com/AcalaNetwork/Acala",
      "rpc": "https://eth-rpc-acala.aca-api.network",
      "documentation": "https://polkadot.js.org/api/substrate/rpc.html"
    }
  },
  {
    "id": "aeternity",
    "name": "Aeternity",
    "coinId": 457,
    "symbol": "AE",
    "decimals": 18,
    "blockchain": "Aeternity",
    "derivation": [
      {
        "path": "m/44'/457'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://explorer.aepps.com",
      "txPath": "/transactions/",
      "accountPath": "/account/transactions/"
    },
    "info": {
      "url": "https://aeternity.com",
      "source": "https://github.com/aeternity/aeternity",
      "rpc": "https://sdk-mainnet.aepps.com",
      "documentation": "http://aeternity.com/api-docs/"
    }
  },
  {
    "id": "kava",
    "name": "Kava",
    "coinId": 459,
    "symbol": "KAVA",
    "decimals": 6,
    "blockchain": "Cosmos",
    "chainId": "kava_2222-10",
    "derivation": [
      {
        "path": "m/44'/459'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "kava",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://mintscan.io/kava",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "2988DF83FCBFAA38179D583A96734CBD071541D6768221BB23111BC8136D5E6A",
      "sampleAccount": "kava1xd39avn2f008jmvua0eupg39zsp2xn3wf802vn"
    },
    "info": {
      "url": "https://kava.io",
      "source": "https://github.com/kava-labs/kava",
      "rpc": "https://data.kava.io",
      "documentation": "https://rpc.kava.io"
    }
  },
  {
    "id": "filecoin",
    "name": "Filecoin",
    "coinId": 461,
    "symbol": "FIL",
    "decimals": 18,
    "blockchain": "Filecoin",
    "derivation": [
      {
        "path": "m/44'/461'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://filfox.info/en",
      "txPath": "/message/",
      "accountPath": "/address/",
      "sampleTx": "bafy2bzacedsgjcd6xfhrrymmfrqubb44otlyhvgqkgsh533d5j5hwniiqespm",
      "sampleAccount": "f1abjxfbp274xpdqcpuaykwkfb43omjotacm2p3za"
    },
    "info": {
      "url": "https://filecoin.io/",
      "source": "https://github.com/filecoin-project/lotus",
      "rpc": "",
      "documentation": "https://docs.lotu.sh"
    }
  },
  {
    "id": "bluzelle",
    "name": "Bluzelle",
    "coinId": 483,
    "symbol": "BLZ",
    "decimals": 6,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/483'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "bluzelle",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://bigdipper.net.bluzelle.com",
      "txPath": "/transactions/",
      "accountPath": "/account/",
      "sampleTx": "AC026E0EC6E33A77D5EA6B9CEF9810699BC2AD8C5582E007E7857457C6D3B819",
      "sampleAccount": "bluzelle1q9cryfal7u3jvnq6er5ufety20xtzw6ycx2te9"
    },
    "info": {
      "url": "https://bluzelle.com",
      "source": "https://github.com/bluzelle",
      "rpc": "https://bluzelle.github.io/api/",
      "documentation": "https://docs.bluzelle.com/developers/"
    }
  },
  {
    "id": "band",
    "name": "BandChain",
    "symbol": "BAND",
    "coinId": 494,
    "decimals": 6,
    "blockchain": "Cosmos",
    "chainId": "laozi-mainnet",
    "derivation": [
      {
        "path": "m/44'/494'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "band",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/band",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "74AF38C2183B06EB6274DA4AAC0D2334E6E283643D436852F5E088AEA2CD0B17",
      "sampleAccount": "band16gpgu994g2gdrzvwp9047le3pcq9wz6mcgtd4w"
    },
    "info": {
      "url": "https://bandprotocol.com/",
      "source": "https://github.com/bandprotocol/bandchain",
      "rpc": "https://api-wt2-lb.bandchain.org",
      "documentation": "https://docs.bandchain.org/"
    }
  },
  {
    "id": "theta",
    "name": "Theta",
    "coinId": 500,
    "symbol": "THETA",
    "decimals": 18,
    "blockchain": "Theta",
    "derivation": [
      {
        "path": "m/44'/500'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://explorer.thetatoken.org",
      "txPath": "/txs/",
      "accountPath": "/account/"
    },
    "info": {
      "url": "https://www.thetatoken.org",
      "source": "https://github.com/thetatoken/theta-protocol-ledger",
      "rpc": "",
      "documentation": "https://github.com/thetatoken/theta-mainnet-integration-guide/blob/master/docs/api.md#api-reference"
    }
  },
  {
    "id": "tfuelevm",
    "name": "Theta Fuel",
    "coinId": 361,
    "symbol": "TFUEL",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/500'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "361",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.thetatoken.org",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "0xdb1c1c4e06289a4fc71b98ced218242d4f4a54a09987791a6a53a5260c053555",
      "sampleAccount": "0xa144e6a98b967e585b214bfa7f6692af81987e5b"
    },
    "info": {
      "url": "https://www.thetatoken.org",
      "source": "https://github.com/thetatoken/theta-protocol-ledger",
      "rpc": "https://eth-rpc-api.thetatoken.org/rpc",
      "documentation": "https://github.com/thetatoken/theta-mainnet-integration-guide/blob/master/docs/api.md#api-reference"
    }
  },
  {
    "id": "solana",
    "name": "Solana",
    "coinId": 501,
    "symbol": "SOL",
    "decimals": 9,
    "blockchain": "Solana",
    "derivation": [
      {
        "path": "m/44'/501'/0'"
      },
      {
        "name": "solana",
        "path": "m/44'/501'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://solscan.io",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "5LmxrEKGchhMuYfw6Qut6CbsvE9pVfb8YvwZKvWssSesDVjHioBCmWKSJQh1WhvcM6CpemhpHNmEMA2a36rzwTa8",
      "sampleAccount": "Bxp8yhH9zNwxyE4UqxP7a7hgJ5xTZfxNNft7YJJ2VRjT"
    },
    "info": {
      "url": "https://solana.com",
      "source": "https://github.com/solana-labs/solana",
      "rpc": "https://api.mainnet-beta.solana.com",
      "documentation": "https://docs.solana.com"
    }
  },
  {
    "id": "elrond",
    "name": "MultiversX",
    "coinId": 508,
    "symbol": "eGLD",
    "decimals": 18,
    "blockchain": "MultiversX",
    "derivation": [
      {
        "path": "m/44'/508'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "hrp": "erd",
    "explorer": {
      "url": "https://explorer.multiversx.com",
      "txPath": "/transactions/",
      "accountPath": "/accounts/"
    },
    "info": {
      "url": "https://multiversx.com/",
      "source": "https://github.com/multiversx/mx-chain-go",
      "rpc": "https://api.multiversx.com",
      "documentation": "https://docs.multiversx.com"
    }
  },
  {
    "id": "binance",
    "name": "Binance",
    "displayName": "BNB Beacon Chain",
    "coinId": 714,
    "symbol": "BNB",
    "decimals": 8,
    "blockchain": "Binance",
    "derivation": [
      {
        "path": "m/44'/714'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "addressHasher": "sha256ripemd",
    "hrp": "bnb",
    "chainId": "Binance-Chain-Tigris",
    "explorer": {
      "url": "https://explorer.binance.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "A93625C9F9ABEA1A8E31585B30BBB16C34FAE0D172EB5B6B2F834AF077BF06BB",
      "sampleAccount": "bnb1u7jm0cll5h3224y0tapwn6gf6pr49ytewx4gsz"
    },
    "info": {
      "url": "https://www.bnbchain.org",
      "source": "https://github.com/bnb-chain/node-binary",
      "rpc": "https://dex.binance.org",
      "documentation": "https://docs.bnbchain.org/docs/beaconchain/develop/api-reference/dex-api/paths"
    }
  },
  {
    "id": "tbinance",
    "name": "TBinance",
    "displayName": "TBNB",
    "coinId": 30000714,
    "slip44": 714,
    "symbol": "BNB",
    "decimals": 8,
    "blockchain": "Binance",
    "derivation": [
      {
        "path": "m/44'/714'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "addressHasher": "sha256ripemd",
    "hrp": "tbnb",
    "explorer": {
      "url": "https://testnet-explorer.binance.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "92E9DA1B6D603667E2DE83C0AC0C1D9E6D65405AD642DA794421C64A82A078D0",
      "sampleAccount": "tbnb1c2cxgv3cklswxlvqr9anm6mlp6536qnd36txgr"
    },
    "info": {
      "url": "https://www.bnbchain.org",
      "source": "https://github.com/bnb-chain/node-binary",
      "rpc": "https://testnet-dex.binance.org",
      "documentation": "https://docs.bnbchain.org/docs/beaconchain/develop/api-reference/dex-api/paths-testnet"
    }
  },
  {
    "id": "vechain",
    "name": "VeChain",
    "coinId": 818,
    "symbol": "VET",
    "decimals": 18,
    "blockchain": "Vechain",
    "derivation": [
      {
        "path": "m/44'/818'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "74",
    "explorer": {
      "url": "https://explore.vechain.org",
      "txPath": "/transactions/",
      "accountPath": "/accounts/",
      "sampleTx": "0xa424053be0063555aee73a595ca69968c2e4d90d36f280753e503b92b11a655d",
      "sampleAccount": "0x8a0a035a33173601bfbec8b6ae7c4a6557a55103"
    },
    "info": {
      "url": "https://vechain.org",
      "source": "https://github.com/vechain/thor",
      "rpc": "",
      "documentation": "https://doc.vechainworld.io/docs"
    }
  },
  {
    "id": "callisto",
    "name": "Callisto",
    "coinId": 820,
    "symbol": "CLO",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/820'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "820",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.callisto.network",
      "txPath": "/tx/",
      "accountPath": "/addr/"
    },
    "info": {
      "url": "https://callisto.network",
      "source": "https://github.com/EthereumCommonwealth/go-callisto",
      "rpc": "https://clo-geth.0xinfra.com",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "neo",
    "name": "NEO",
    "coinId": 888,
    "symbol": "NEO",
    "decimals": 8,
    "blockchain": "NEO",
    "derivation": [
      {
        "path": "m/44'/888'/0'/0/0"
      }
    ],
    "curve": "nist256p1",
    "publicKeyType": "nist256p1",
    "explorer": {
      "url": "https://neoscan.io",
      "txPath": "/transaction/",
      "accountPath": "/address/",
      "sampleTx": "e0ddf7c81c732df26180aca0c36d5868ad009fdbbe6e7a56ebafc14bba41cd53",
      "sampleAccount": "AcxuqWhTureEQGeJgbmtSWNAtssjMLU7pb"
    },
    "info": {
      "url": "https://neo.org",
      "source": "https://github.com/neo-project/neo",
      "rpc": "http://seed1.ngd.network:10332",
      "documentation": "https://neo.org/eco"
    }
  },
  {
    "id": "viction",
    "name": "Viction",
    "coinId": 889,
    "symbol": "VIC",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/889'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "88",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://www.vicscan.xyz",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x35a8d3ab06c94d5b7d27221b7c9a24ba3f1710dd0fcfd75c5d59b3a885fd709b",
      "sampleAccount": "0x86cCbD9bfb371c355202086882bC644A7D0b024B"
    },
    "info": {
      "url": "https://www.viction.xyz/",
      "source": "https://github.com/BuildOnViction/tomochain",
      "rpc": "https://rpc.tomochain.com",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "bitcoindiamond",
    "name": "Bitcoin Diamond",
    "coinId": 999,
    "symbol": "BCD",
    "decimals": 7,
    "blockchain": "BitcoinDiamond",
    "derivation": [
      {
        "path": "m/84'/999'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 0,
    "p2shPrefix": 5,
    "hrp": "bcd",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "http://explorer.btcd.io/#",
      "txPath": "/tx?tx=",
      "accountPath": "/address?address=",
      "sampleTx": "ec564fe8993ba77f3f5c8b7f6ebb4cbc08e564a54612d6f4584cd1017cf723d4",
      "sampleAccount": "1HNTyntGXNhy4WxNzWfffPqp7LHb8bGJ9R"
    },
    "info": {
      "url": "https://www.bitcoindiamond.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "thundertoken",
    "name": "ThunderCore",
    "coinId": 1001,
    "symbol": "TT",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/1001'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "108",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://scan.thundercore.com",
      "txPath": "/transactions/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://thundercore.com",
      "source": "https://github.com/thundercore/pala",
      "rpc": "https://mainnet-rpc.thundercore.com",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "harmony",
    "name": "Harmony",
    "coinId": 1023,
    "symbol": "ONE",
    "decimals": 18,
    "blockchain": "Harmony",
    "derivation": [
      {
        "path": "m/44'/1023'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "one",
    "explorer": {
      "url": "https://explorer.harmony.one",
      "txPath": "/#/tx/",
      "accountPath": "/#/address/"
    },
    "info": {
      "url": "https://harmony.one",
      "source": "https://github.com/harmony-one/go-sdk",
      "rpc": "",
      "documentation": "https://docs.harmony.one/home/harmony-networks/harmony-network-overview/mainnet"
    }
  },
  {
    "id": "oasis",
    "name": "Oasis",
    "coinId": 474,
    "symbol": "ROSE",
    "decimals": 9,
    "blockchain": "OasisNetwork",
    "derivation": [
      {
        "path": "m/44'/474'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "hrp": "oasis",
    "explorer": {
      "url": "https://oasisscan.com",
      "txPath": "/transactions/",
      "accountPath": "/accounts/detail/",
      "sampleTx": "73dc977fdd8596d4a57e6feb891b21f5da3652d26815dc94f15f7420c298e29e",
      "sampleAccount": "oasis1qrx376dmwuckmruzn9vq64n49clw72lywctvxdf4"
    },
    "info": {
      "url": "https://oasisprotocol.org/",
      "source": "https://github.com/oasisprotocol/oasis-core",
      "rpc": "https://rosetta.oasis.dev/api/v1",
      "documentation": "https://docs.oasis.dev/oasis-core/"
    }
  },
  {
    "id": "ontology",
    "name": "Ontology",
    "coinId": 1024,
    "symbol": "ONT",
    "decimals": 0,
    "blockchain": "Ontology",
    "derivation": [
      {
        "path": "m/44'/1024'/0'/0/0"
      }
    ],
    "curve": "nist256p1",
    "publicKeyType": "nist256p1",
    "explorer": {
      "url": "https://explorer.ont.io",
      "txPath": "/transaction/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://ont.io",
      "source": "https://github.com/ontio/ontology",
      "rpc": "http://dappnode1.ont.io:20336",
      "documentation": "https://github.com/ontio/ontology/blob/master/docs/specifications/rpc_api.md"
    }
  },
  {
    "id": "tezos",
    "name": "Tezos",
    "coinId": 1729,
    "symbol": "XTZ",
    "decimals": 6,
    "blockchain": "Tezos",
    "derivation": [
      {
        "path": "m/44'/1729'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://tzstats.com",
      "txPath": "/",
      "accountPath": "/",
      "sampleTx": "onk3Z6V4StyfiXTPSHwZFvTKVAaws37cHmZacmULPr3VbVHpKrg",
      "sampleAccount": "tz1SiPXX4MYGNJNDsRc7n8hkvUqFzg8xqF9m"
    },
    "info": {
      "url": "https://tezos.com",
      "source": "https://gitlab.com/tezos/tezos",
      "rpc": "https://rpc.tulip.tools/mainnet",
      "documentation": "https://tezos.gitlab.io/tezos/api/rpc.html"
    }
  },
  {
    "id": "cardano",
    "name": "Cardano",
    "coinId": 1815,
    "symbol": "ADA",
    "decimals": 6,
    "blockchain": "Cardano",
    "derivation": [
      {
        "path": "m/1852'/1815'/0'/0/0"
      }
    ],
    "curve": "ed25519ExtendedCardano",
    "publicKeyType": "ed25519Cardano",
    "hrp": "addr",
    "explorer": {
      "url": "https://cardanoscan.io",
      "txPath": "/transaction/",
      "accountPath": "/address/",
      "sampleTx": "b7a6c5cadab0f64bdc89c77ee4a351463aba5c33f2cef6bbd6542a74a90a3af3",
      "sampleAccount": "DdzFFzCqrhstpwKc8WMvPwwBb5oabcTW9zc5ykA37wJR4tYQucvsR9dXb2kEGNXkFJz2PtrpzfRiZkx8R1iNo8NYqdsukVmv7EAybFwC"
    },
    "info": {
      "url": "https://www.cardano.org",
      "source": "https://github.com/input-output-hk/cardano-sl",
      "rpc": "",
      "documentation": "https://cardanodocs.com/introduction/"
    }
  },
  {
    "id": "kin",
    "name": "Kin",
    "coinId": 2017,
    "symbol": "KIN",
    "decimals": 5,
    "blockchain": "Stellar",
    "derivation": [
      {
        "path": "m/44'/2017'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://www.kin.org",
      "txPath": "/blockchainInfoPage/?&dataType=public&header=Transaction&id=",
      "accountPath": "/blockchainAccount/?&dataType=public&header=accountID&id="
    },
    "info": {
      "url": "https://www.kin.org",
      "source": "https://github.com/kinecosystem/go",
      "rpc": "https://horizon.kinfederation.com",
      "documentation": "https://www.stellar.org/developers/horizon/reference"
    },
    "deprecated": 'true'
  },
  {
    "id": "qtum",
    "name": "Qtum",
    "coinId": 2301,
    "symbol": "QTUM",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "legacy",
        "path": "m/44'/2301'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      },
      {
        "name": "segwit",
        "path": "m/84'/2301'/0'/0/0",
        "xpub": "zpub",
        "xprv": "zprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 58,
    "p2shPrefix": 50,
    "hrp": "qc",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://qtum.info",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://qtum.org",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "nebulas",
    "name": "Nebulas",
    "coinId": 2718,
    "symbol": "NAS",
    "decimals": 18,
    "blockchain": "Nebulas",
    "derivation": [
      {
        "path": "m/44'/2718'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://explorer.nebulas.io",
      "txPath": "/#/tx/",
      "accountPath": "/#/address/"
    },
    "info": {
      "url": "https://nebulas.io",
      "source": "https://github.com/nebulasio/go-nebulas",
      "rpc": "https://mainnet.nebulas.io",
      "documentation": "https://wiki.nebulas.io/en/latest/dapp-development/rpc/rpc.html"
    }
  },
  {
    "id": "gochain",
    "name": "GoChain",
    "coinId": 6060,
    "symbol": "GO",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/6060'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "60",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.gochain.io",
      "txPath": "/tx/",
      "accountPath": "/addr/"
    },
    "info": {
      "url": "https://gochain.io",
      "source": "https://github.com/gochain-io/gochain",
      "rpc": "https://rpc.gochain.io",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "nuls",
    "name": "NULS",
    "coinId": 8964,
    "symbol": "NULS",
    "decimals": 8,
    "blockchain": "NULS",
    "derivation": [
      {
        "path": "m/44'/8964'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "explorer": {
      "url": "https://nulscan.io",
      "txPath": "/transaction/info?hash=",
      "accountPath": "/address/info?address=",
      "sampleTx": "303e0e42c28acc37ba952a1effd43daa1caec79928054f7abefb21c32e6fdc02",
      "sampleAccount": "NULSd6HgdSjUZy7jKMZfvQ5QU6Z97oufGTGcF"
    },
    "info": {
      "url": "https://nuls.io",
      "source": "https://github.com/nuls-io/nuls-v2",
      "rpc": "https://public1.nuls.io/",
      "documentation": "https://docs.nuls.io/"
    }
  },
  {
    "id": "zelcash",
    "name": "Zelcash",
    "displayName": "Flux",
    "coinId": 19167,
    "symbol": "FLUX",
    "decimals": 8,
    "blockchain": "Zcash",
    "derivation": [
      {
        "path": "m/44'/19167'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "staticPrefix": 28,
    "p2pkhPrefix": 184,
    "p2shPrefix": 189,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.runonflux.io",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://runonflux.io",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "https://blockbook.runonflux.io",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "wanchain",
    "name": "Wanchain",
    "coinId": 5718350,
    "symbol": "WAN",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/5718350'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "888",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://www.wanscan.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x180ea96a3218b82b9b35d796823266d8a425c182507adfe5eeffc96e6a14d856",
      "sampleAccount": "0x69B492D57bb777e97aa7044D0575228434e2E8B1"
    },
    "info": {
      "url": "https://wanchain.org",
      "source": "https://github.com/wanchain/go-wanchain",
      "rpc": "",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "waves",
    "name": "Waves",
    "coinId": 5741564,
    "symbol": "WAVES",
    "decimals": 8,
    "blockchain": "Waves",
    "derivation": [
      {
        "path": "m/44'/5741564'/0'/0'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "curve25519",
    "explorer": {
      "url": "https://wavesexplorer.com",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://wavesplatform.com",
      "source": "https://github.com/wavesplatform/Waves",
      "rpc": "https://nodes.wavesnodes.com",
      "documentation": "https://nodes.wavesnodes.com/api-docs/index.html"
    }
  },
  {
    "id": "bsc",
    "name": "Smart Chain Legacy",
    "coinId": 10000714,
    "slip44": 714,
    "symbol": "BNB",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/714'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "56",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://bscscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xb9ae2e808fe8e57171f303ad8f6e3fd17d949b0bfc7b4db6e8e30a71cc517d7e",
      "sampleAccount": "0x35552c16704d214347f29Fa77f77DA6d75d7C752"
    },
    "info": {
      "url": "https://www.binance.org/en/smartChain",
      "source": "https://github.com/binance-chain/bsc",
      "rpc": "https://data-seed-prebsc-1-s1.binance.org:8545",
      "documentation": "https://eth.wiki/json-rpc/API"
    },
    "deprecated": 'true',
    "testFolderName": "Binance"
  },
  {
    "id": "smartchain",
    "name": "Smart Chain",
    "displayName": "BNB Smart Chain",
    "coinId": 20000714,
    "slip44": 714,
    "symbol": "BNB",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "56",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://bscscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xb9ae2e808fe8e57171f303ad8f6e3fd17d949b0bfc7b4db6e8e30a71cc517d7e",
      "sampleAccount": "0x35552c16704d214347f29Fa77f77DA6d75d7C752"
    },
    "info": {
      "url": "https://www.binance.org/en/smartChain",
      "source": "https://github.com/binance-chain/bsc",
      "rpc": "https://bsc-dataseed1.binance.org",
      "documentation": "https://eth.wiki/json-rpc/API"
    },
    "testFolderName": "Binance"
  },
  {
    "id": "polygon",
    "name": "Polygon",
    "coinId": 966,
    "symbol": "MATIC",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "137",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://polygonscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xe26ed1470d5bf99a53d687843e7acdf7e4ba6620af93b4d672e714de90476e8e",
      "sampleAccount": "0x720E1fa107A1Df39Db4E78A3633121ac36Bec132"
    },
    "info": {
      "url": "https://polygon.technology",
      "source": "https://github.com/maticnetwork/contracts",
      "rpc": "https://polygon-rpc.com",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "rootstock",
    "name": "Rootstock",
    "coinId": 137,
    "symbol": "RBTC",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/137'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "30",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.rsk.co",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xeb8fa0488a655f8dc975153bffd066800bcaae5f21cf372356365b2a1d6d2288",
      "sampleAccount": "0x4e5dabc28e4a0f5e5b19fcb56b28c5a1989352c1"
    },
    "info": {
      "url": "https://rootstock.io",
      "source": "https://github.com/rsksmart/rskj",
      "rpc": "https://public-node.rsk.co",
      "documentation": "https://dev.rootstock.io"
    }
  },
  {
    "id": "thorchain",
    "name": "THORChain",
    "coinId": 931,
    "symbol": "RUNE",
    "decimals": 8,
    "blockchain": "Thorchain",
    "derivation": [
      {
        "path": "m/44'/931'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "thor",
    "addressHasher": "sha256ripemd",
    "chainId": "thorchain-mainnet-v1",
    "explorer": {
      "url": "https://viewblock.io/thorchain",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "ADF0899E58C177E2391F22D04E9C5E1C35BB0F75B42B363A0761687907FD9476",
      "sampleAccount": "thor196yf4pq80hjrmz7nnh0ar0ypqg02r0w4dq4mzu"
    },
    "info": {
      "url": "https://thorchain.org",
      "source": "https://gitlab.com/thorchain/thornode",
      "rpc": "https://seed.thorchain.info",
      "documentation": "https://docs.thorchain.org"
    }
  },
  {
    "id": "optimism",
    "name": "Optimism",
    "displayName": "OP Mainnet",
    "coinId": 10000070,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "10",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://optimistic.etherscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x6fd99288be9bf71eb002bb31da10a4fb0fbbb3c45ae73693b212f49c9db7df8f",
      "sampleAccount": "0x1f932361e31d206b4f6b2478123a9d0f8c761031"
    },
    "info": {
      "url": "https://optimism.io/",
      "source": "https://github.com/ethereum-optimism/optimism",
      "rpc": "https://mainnet.optimism.io",
      "documentation": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "polygonzkevm",
    "name": "Polygon zkEVM",
    "displayName": "Polygon zkEVM",
    "coinId": 10001101,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1101",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://zkevm.polygonscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://www.polygon.technology/",
      "source": "https://github.com/0xpolygonhermez",
      "rpc": "https://zkevm-rpc.com",
      "documentation": "https://wiki.polygon.technology/docs/zkEVM/introduction/"
    }
  },
  {
    "id": "zksync",
    "name": "Zksync",
    "displayName": "zkSync Era",
    "coinId": 10000324,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "324",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.zksync.io",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://portal.zksync.io/",
      "source": "https://github.com/matter-labs/zksync",
      "rpc": "https://zksync2-mainnet.zksync.io",
      "documentation": "https://era.zksync.io/docs"
    }
  },
  {
    "id": "scroll",
    "name": "Scroll",
    "displayName": "Scroll",
    "coinId": 534352,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "534352",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://scrollscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xa2062a4530b194a438bb9f9e87cdce59f70775a52e8336892364445847c43ca2",
      "sampleAccount": "0xf9062b8a30e0d7722960e305049fa50b86ba6253"
    },
    "info": {
      "url": "https://scroll.io",
      "source": "https://github.com/scroll-tech",
      "rpc": "https://rpc.scroll.io",
      "documentation": "https://guide.scroll.io"
    }
  },
  {
    "id": "arbitrum",
    "name": "Arbitrum",
    "coinId": 10042221,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "42161",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://arbiscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xa1e319be22c08155e5904aa211fb87df5f4ade48de79c6578b1cf3dfda9e498c",
      "sampleAccount": "0xecf9ffa7f51e1194f89c25ad8c484f6bfd04e1ac"
    },
    "info": {
      "url": "https://arbitrum.io",
      "source": "https://github.com/OffchainLabs/arbitrum",
      "rpc": "https://arb1.arbitrum.io/rpc",
      "documentation": "https://docs.arbitrum.io/"
    }
  },
  {
    "id": "arbitrumnova",
    "name": "Arbitrum Nova",
    "coinId": 10042170,
    "slip44": 60,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "42170",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://nova.arbiscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xfdfee13848c2d21813c82c53afc9925f31770564c3117477960a81055702c1be",
      "sampleAccount": "0x0d0707963952f2fba59dd06f2b425ace40b492fe"
    },
    "info": {
      "url": "https://nova.arbitrum.io",
      "source": "https://github.com/OffchainLabs/arbitrum",
      "rpc": "https://nova.arbitrum.io/rpc",
      "documentation": "https://docs.arbitrum.io/"
    }
  },
  {
    "id": "heco",
    "name": "ECO Chain",
    "displayName": "Huobi ECO Chain",
    "coinId": 10000553,
    "slip44": 553,
    "symbol": "HT",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "128",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://hecoinfo.com",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://www.hecochain.com/en-us",
      "source": "https://github.com/HuobiGroup/huobi-eco-chain",
      "rpc": "https://http-mainnet-node.huobichain.com",
      "documentation": "https://eth.wiki/json-rpc/API"
    },
    "testFolderName": "ECO"
  },
  {
    "id": "avalanchec",
    "name": "Avalanche C-Chain",
    "coinId": 10009000,
    "symbol": "AVAX",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "43114",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://snowtrace.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x9243890b844219accefd8798271052f5a056453ec18984a56e81c92921330d54",
      "sampleAccount": "0xa664325f36Ec33E66323fe2620AF3f2294b2Ef3A"
    },
    "info": {
      "url": "https://www.avalabs.org/",
      "client": "https://github.com/ava-labs/avalanchego",
      "clientPublic": "https://api.avax.network/ext/bc/C/rpc",
      "clientDocs": "https://docs.avax.network/"
    },
    "testFolderName": "Avalanche"
  },
  {
    "id": "xdai",
    "name": "xDai",
    "displayName": "Gnosis Chain",
    "coinId": 10000100,
    "symbol": "xDAI",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "100",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blockscout.com/xdai/mainnet",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x936798a1ef607c9e856d7861b15999c770c06f0887c4fc1f6acbf3bef09899c1",
      "sampleAccount": "0x12d61a95CF55e18D267C2F1AA67d8e42ae1368f8"
    },
    "info": {
      "url": "https://www.xdaichain.com",
      "client": "https://github.com/openethereum/openethereum",
      "clientPublic": "https://rpc.gnosischain.com",
      "clientDocs": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "fantom",
    "name": "Fantom",
    "coinId": 10000250,
    "symbol": "FTM",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "250",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://ftmscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xb0a741d882291951de1fac72e90b9baf886ddb0c9c87658a0c206490dfaa5202",
      "sampleAccount": "0x9474feb9917b87da6f0d830ba66ee0035835c0d3"
    },
    "info": {
      "url": "https://fantom.foundation",
      "client": "https://github.com/openethereum/openethereum",
      "clientPublic": "https://rpc.ftm.tools",
      "clientDocs": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "cryptoorg",
    "name": "CryptoOrg",
    "displayName": "Crypto.org",
    "coinId": 394,
    "symbol": "CRO",
    "decimals": 8,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/394'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "cro",
    "chainId": "crypto-org-chain-mainnet-1",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://crypto.org/explorer",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "D87D2EB46B21466886EE149C1DEA3AE6C2E019C7D8C24FA1533A95439DDCE1E2",
      "sampleAccount": "cro10wrflcdc4pys9vvgqm98yg7yv5ltj7d3xehent"
    },
    "info": {
      "url": "https://crypto.org/",
      "client": "https://github.com/crypto-org-chain/chain-main",
      "clientPublic": "https://mainnet.crypto.org:1317/",
      "clientDocs": "https://crypto.org/docs/resources/chain-integration.html#api-documentation"
    }
  },
  {
    "id": "celo",
    "name": "Celo",
    "coinId": 52752,
    "symbol": "CELO",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "42220",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.celo.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xaf41ee58afe633dc7b179c15693cca40fe0372c1d7c70351620105d59d326693",
      "sampleAccount": "0xFBFf95e2Fa7e4Ff3aeA34eFB05fB60F9968a6aaD"
    },
    "info": {
      "url": "https://celo.org",
      "client": "https://github.com/celo-org/celo-blockchain",
      "clientPublic": "https://forno.celo.org",
      "clientDocs": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "ronin",
    "name": "Ronin",
    "coinId": 10002020,
    "slip44": 60,
    "symbol": "RON",
    "decimals": 18,
    "blockchain": "Ronin",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "2020",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.roninchain.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xc09835aaf9c1cacea8ce322865583c791d3a4dfbd9a3b72f79539db88d3697ab",
      "sampleAccount": "0xdc05ecd5fbdb64058d94f3182d66f44342b9adcb"
    },
    "info": {
      "url": "https://whitepaper.axieinfinity.com/technology/ronin-ethereum-sidechain",
      "client": "https://github.com/axieinfinity/ronin-smart-contracts",
      "clientPublic": "https://api.roninchain.com/rpc",
      "clientDocs": "https://eth.wiki/json-rpc/API"
    }
  },
  {
    "id": "secret",
    "name": "Secret",
    "displayName": "Secret",
    "coinId": 529,
    "symbol": "SCRT",
    "decimals": 6,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/529'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "secret",
    "chainId": "secret-4",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://mintscan.io/secret",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "026B4886B1D9CE836A99755DDE99D4F8A7748D27B1CE9D298A763B1CFFF62C00",
      "sampleAccount": "secret167m3s89ddurjpyr82vsluvvj0t8ylzn95trrqy"
    },
    "info": {
      "url": "https://scrt.network/",
      "source": "https://github.com/scrtlabs/SecretNetwork",
      "rpc": "https://scrt-rpc.blockpane.com/",
      "documentation": "https://docs.scrt.network/"
    }
  },
  {
    "id": "osmosis",
    "name": "Osmosis",
    "displayName": "Osmosis",
    "coinId": 10000118,
    "symbol": "OSMO",
    "decimals": 6,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "osmo",
    "chainId": "osmosis-1",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://mintscan.io/osmosis",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "5A6E50A6F2927E4B8C87BB094D5FBF15F1287429A09111806FC44B3CD86CACA8",
      "sampleAccount": "osmo1mky69cn8ektwy0845vec9upsdphktxt0en97f5"
    },
    "info": {
      "url": "https://osmosis.zone/",
      "client": "https://github.com/osmosis-labs/osmosis",
      "clientPublic": "https://rpc-osmosis.keplr.app/",
      "clientDocs": ""
    }
  },
  {
    "id": "ecash",
    "name": "eCash",
    "coinId": 899,
    "symbol": "XEC",
    "decimals": 2,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "path": "m/44'/899'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 0,
    "p2shPrefix": 5,
    "hrp": "ecash",
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.bitcoinabc.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "6bc767e69cfacffd954c9e5acd178d3140bf00d094b92c6f6052b517500c553b",
      "sampleAccount": "ecash:pqnqv9lt7e5vjyp0w88zf2af0l92l8rxdg2jj94l5j"
    },
    "info": {
      "url": "https://e.cash",
      "source": "https://github.com/trezor/blockbook",
      "rpc": "https://blockbook.fabien.cash:9197",
      "documentation": "https://github.com/trezor/blockbook/blob/master/docs/api.md"
    }
  },
  {
    "id": "iost",
    "name": "IOST",
    "coinId": 291,
    "symbol": "IOST",
    "decimals": 2,
    "blockchain": "IOST",
    "derivation": [
      {
        "path": "m/44'/899'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "p2pkhPrefix": 0,
    "p2shPrefix": 5,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.iost.io",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "7dKQzgTkPBNrZqrQ2Bqhqq132CHGPKANFDtzRsjHRCqx",
      "sampleAccount": "4av8w81EyzUgHonsVWqfs15WM4Vrpgox4BYYQWhNQDVu"
    },
    "info": {
      "url": "https://iost.io",
      "source": "https://github.com/iost-official/go-iost",
      "rpc": "",
      "documentation": "https://developers.iost.io/docs/en/6-reference/API.html"
    }
  },
  {
    "id": "cronos",
    "name": "Cronos Chain",
    "coinId": 10000025,
    "symbol": "CRO",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "25",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://cronoscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://cronos.org",
      "client": "https://github.com/crypto-org-chain/cronos",
      "clientPublic": "https://evm-cronos.crypto.org",
      "clientDocs": "https://eth.wiki/json-rpc/API"
    },
    "testFolderName": "Cronos"
  },
  {
    "id": "kavaevm",
    "name": "KavaEvm",
    "coinId": 10002222,
    "symbol": "KAVA",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "2222",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.kava.io",
      "txPath": "/tx/",
      "accountPath": "/address/"
    },
    "info": {
      "url": "https://www.kava.io/",
      "client": "https://github.com/Kava-Labs/kava",
      "documentation": "https://docs.kava.io/docs/ethereum/overview/",
      "rpc": "https://evm.kava.io"
    }
  },
  {
    "id": "smartbch",
    "name": "Smart Bitcoin Cash",
    "coinId": 10000145,
    "symbol": "BCH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "10000",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://www.smartscan.cash",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x6413466b455b17d03c7a8ce2d7f99fec34bcd338628bdd2d0580a21e3197a4d9",
      "sampleAccount": "0xFeEc227410E1DF9f3b4e6e2E284DC83051ae468F"
    },
    "info": {
      "url": "https://smartbch.org/",
      "source": "https://github.com/smartbch/smartbch",
      "rpc": "https://smartbch.fountainhead.cash/mainnet",
      "documentation": "https://github.com/smartbch/docs/blob/main/developers-guide/jsonrpc.md"
    },
    "testFolderName": "Bitcoin"
  },
  {
    "id": "kcc",
    "name": "KuCoin Community Chain",
    "coinId": 10000321,
    "symbol": "KCS",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "321",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.kcc.io/en",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x2f0d79cd289a02f3181b68b9583a64c3809fe7387810b274275985c29d02c80d",
      "sampleAccount": "0x4446fc4eb47f2f6586f9faab68b3498f86c07521"
    },
    "info": {
      "url": "https://www.kcc.io/",
      "source": "https://github.com/kcc-community/kcc",
      "rpc": "https://rpc-mainnet.kcc.network",
      "documentation": "https://docs.kcc.io/#/en-us/"
    },
    "testFolderName": "KuCoinCommunityChain"
  },
  {
    "id": "boba",
    "name": "Boba",
    "coinId": 10000288,
    "symbol": "BOBAETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "288",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blockexplorer.boba.network",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x31533707c3feb3b10f7deeea387ff8893f229253e65ca6b14d2400bf95b5d103",
      "sampleAccount": "0x4F96F50eDB37a19216d87693E5dB241e31bD3735"
    },
    "info": {
      "url": "https://boba.network/",
      "source": "https://github.com/bobanetwork/boba",
      "rpc": "https://mainnet.boba.network",
      "documentation": "https://docs.boba.network/"
    }
  },
  {
    "id": "metis",
    "name": "Metis",
    "coinId": 10001088,
    "symbol": "METIS",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1088",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://andromeda-explorer.metis.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x422f2ebbede32d4434ad0cf0ae55d44a84e14d3d5725a760133255b42676d8ce",
      "sampleAccount": "0xBe9E8Ec25866B21bA34e97b9393BCabBcB4A5C86"
    },
    "info": {
      "url": "https://www.metis.io/",
      "source": "https://github.com/MetisProtocol/mvm",
      "rpc": "https://andromeda.metis.io/?owner=1088",
      "documentation": "https://docs.metis.io/"
    }
  },
  {
    "id": "aurora",
    "name": "Aurora",
    "coinId": 1323161554,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1313161554",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://aurorascan.dev",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x99deebdb70f8027037abb3d3d0f3c7523daee857d85e9056d2671593ff2f2f28",
      "sampleAccount": "0x8707cdE20dd43E3dB1F74c28fcd509ef38B0bA51"
    },
    "info": {
      "url": "https://aurora.dev/",
      "source": "https://github.com/aurora-is-near/aurora-engine",
      "rpc": "https://mainnet.aurora.dev/",
      "documentation": "https://doc.aurora.dev/"
    }
  },
  {
    "id": "evmos",
    "name": "Evmos",
    "coinId": 10009001,
    "symbol": "EVMOS",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "9001",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://evm.evmos.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x24af42cf4977a96d62e3a82c3cd9b519c3e7c53dd83398b88f0cb435d867b422",
      "sampleAccount": "0x30627903124Aa1e71384bc52e1cb96E4AB3252b6"
    },
    "info": {
      "url": "https://evmos.org/",
      "source": "https://github.com/tharsis/evmos",
      "rpc": "https://eth.bd.evmos.org:8545",
      "documentation": "https://docs.evmos.org/"
    }
  },
  {
    "id": "nativeevmos",
    "name": "NativeEvmos",
    "displayName": "Native Evmos",
    "coinId": 20009001,
    "symbol": "EVMOS",
    "decimals": 18,
    "blockchain": "NativeEvmos",
    "chainId": "evmos_9001-2",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "evmos",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://mintscan.io/evmos",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "A16C211C83AD1E684DE46F694FAAC17D8465C864BD7385A81EC062CDE0638811",
      "sampleAccount": "evmos17xpfvakm2amg962yls6f84z3kell8c5ljcjw34"
    },
    "info": {
      "url": "https://evmos.org/",
      "client": "https://github.com/tharsis/evmos",
      "clientPublic": "https://rest.bd.evmos.org:1317",
      "clientDocs": ""
    }
  },
  {
    "id": "moonriver",
    "name": "Moonriver",
    "coinId": 10001285,
    "symbol": "MOVR",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1285",
    "explorer": {
      "url": "https://moonriver.moonscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x2e2daa3943ba65d9bbb910a4f6765aa6a466a0ef8935090547ca9d30e201e032",
      "sampleAccount": "0x899831D937937d011305E73EE782cce0455DF15a"
    },
    "info": {
      "url": "https://moonbeam.network/networks/moonriver",
      "rpc": "https://moonriver.public.blastapi.io"
    }
  },
  {
    "id": "moonbeam",
    "name": "Moonbeam",
    "coinId": 10001284,
    "symbol": "GLMR",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1284",
    "explorer": {
      "url": "https://moonscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xb22a146c933e6e51affbfa5f712a266b5f5e92ae453cd2f252bcc3c36ff035a6",
      "sampleAccount": "0x201bb4f276C765dF7225e5A4153E17edD23a67eC"
    },
    "info": {
      "url": "https://moonbeam.network",
      "rpc": "https://rpc.api.moonbeam.network",
      "documentation": "https://docs.moonbeam.network"
    }
  },
  {
    "id": "klaytn",
    "name": "Klaytn",
    "coinId": 10008217,
    "symbol": "KLAY",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "8217",
    "explorer": {
      "url": "https://scope.klaytn.com",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "0x93ea92687845fe7bb6cacd69c76a16a2a3c2bbb85a8a93ff0e032d0098d583d7",
      "sampleAccount": "0x2ad9656bf5b82caf10847b431012e28e301e83ba"
    },
    "info": {
      "url": "https://klaytn.foundation",
      "rpc": "https://public-node-api.klaytnapi.com/v1/cypress",
      "documentation": "https://docs.klaytn.foundation"
    }
  },
  {
    "id": "meter",
    "name": "Meter",
    "coinId": 18000,
    "chainId": "82",
    "symbol": "MTR",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://scan.meter.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x8ea268d5dbb40217c763b800a75fc063cf28b56f40f2bc69dc043f5c4bbdc144",
      "sampleAccount": "0xe5a273954d24eddf9ae9ea4cef2347d584cfa3dd"
    },
    "info": {
      "url": "https://meter.io/",
      "source": "https://github.com/meterio/meter-pov",
      "rpc": "https://rpc.meter.io",
      "documentation": "https://docs.meter.io/"
    }
  },
  {
    "id": "okc",
    "name": "OKX Chain",
    "coinId": 996,
    "chainId": "66",
    "symbol": "OKT",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://www.oklink.com/oktc",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x46C3A947E8248570FBD28E4FE456CC8F80DFD90716533878FB67857B95FA3D37",
      "sampleAccount": "0x074faafd0b20fad2efa115b8ed7e75993e580b85"
    },
    "info": {
      "url": "https://www.okx.com/okc",
      "source": "https://github.com/okex/exchain",
      "rpc": "https://exchainrpc.okex.org",
      "documentation": "https://okc-docs.readthedocs.io/en/latest"
    }
  },
  {
    "id": "cfxevm",
    "name": "Conflux eSpace",
    "coinId": 1030,
    "chainId": "1030",
    "symbol": "CFX",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://evm.confluxscan.net",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x920efefb3213b2d6a3b84149cb50b61a813d085443a20e1b0eab74120e41ff72",
      "sampleAccount": "0x337a087daef75c72871de592fbbba570829a936a"
    },
    "info": {
      "url": "https://confluxnetwork.org",
      "source": "https://github.com/conflux-chain",
      "rpc": "https://evm.confluxrpc.com",
      "documentation": "https://doc.confluxnetwork.org/docs/espace"
    }
  },
  {
    "id": "greenfield",
    "name": "Greenfield",
    "displayName": "BNB Greenfield",
    "coinId": 5600,
    "symbol": "BNB",
    "decimals": 18,
    "chainId": "1017",
    "blockchain": "Greenfield",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://greenfieldscan.com",
      "txPath": "/tx/",
      "accountPath": "/account/",
      "sampleTx": "0x150eac42070957115fd538b1f348fadd78d710fb641c248120efcf35d1e7e4f3",
      "sampleAccount": "0xcf0f6b88ed72653b00fdebbffc90b98072cb3285"
    },
    "info": {
      "url": "https://greenfield.bnbchain.org",
      "source": "https://github.com/bnb-chain/greenfield",
      "rpc": "https://gnfd-testnet-fullnode-tendermint-us.bnbchain.org",
      "documentation": "https://docs.bnbchain.org/greenfield-docs"
    }
  },
  {
    "id": "opbnb",
    "name": "OpBNB",
    "coinId": 204,
    "chainId": "204",
    "symbol": "BNB",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://opbnbscan.com",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x788ea8fb4a82dae957f1d3b18af3cd0bbde55a276e66bd17af8c869f24c03a0f",
      "sampleAccount": "0x4eaf936c172b5e5511959167e8ab4f7031113ca3"
    },
    "info": {
      "url": "https://opbnb.bnbchain.org/en",
      "source": "https://github.com/bnb-chain/opbnb",
      "rpc": "https://opbnb-mainnet-rpc.bnbchain.org",
      "documentation": "https://docs.bnbchain.org/opbnb-docs"
    }
  },
  {
    "id": "stratis",
    "name": "Stratis",
    "coinId": 105105,
    "symbol": "STRAX",
    "decimals": 8,
    "blockchain": "Bitcoin",
    "derivation": [
      {
        "name": "segwit",
        "path": "m/44'/105105'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "strax",
    "p2pkhPrefix": 75,
    "p2shPrefix": 140,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.rutanio.com/strax/explorer",
      "txPath": "/transaction/",
      "accountPath": "/address/",
      "sampleTx": "3923df87e83859dec8b87a414cbb1529113788c512a4d0c283e1394c274f0bfb",
      "sampleAccount": "XWqnSWzQA5kDAS727UTYtXkdcbKc8mEvyN"
    },
    "info": {
      "url": "https://www.stratisplatform.com/",
      "source": "https://github.com/stratisproject",
      "rpc": "",
      "documentation": "https://academy.stratisplatform.com/index.html"
    }
  },
  {
    "id": "Nebl",
    "name": "Nebl",
    "coinId": 146,
    "symbol": "NEBL",
    "decimals": 8,
    "blockchain": "Verge",
    "derivation": [
      {
        "path": "m/44'/146'/0'/0/0",
        "xpub": "xpub",
        "xprv": "xprv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "p2pkhPrefix": 53,
    "p2shPrefix": 112,
    "publicKeyHasher": "sha256ripemd",
    "base58Hasher": "sha256d",
    "explorer": {
      "url": "https://explorer.nebl.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "1e56c745ab87d702c98eddc6bc2475b2eb292ed4af92d170b2362c8a089272a4",
      "sampleAccount": "NboLGGKWtK5eXzaah5GVpXju9jCcoMi4cc"
    },
    "info": {
      "url": "https://nebl.io",
      "source": "https://github.com/NeblioTeam",
      "rpc": "",
      "documentation": "https://github.com/NeblioTeam"
    }
  },
  {
    "id": "hedera",
    "name": "Hedera",
    "coinId": 3030,
    "symbol": "HBAR",
    "decimals": 8,
    "blockchain": "Hedera",
    "derivation": [
      {
        "path": "m/44'/3030'/0'/0'/0"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://hashscan.io/mainnet",
      "txPath": "/transaction/",
      "accountPath": "/account/",
      "sampleTx": "0.0.19790-1666769504-858851231",
      "sampleAccount": "0.0.19790"
    },
    "info": {
      "url": "https://hedera.com/",
      "source": "https://github.com/hashgraph",
      "documentation": "https://docs.hedera.com"
    }
  },
  {
    "id": "agoric",
    "name": "Agoric",
    "coinId": 564,
    "symbol": "BLD",
    "decimals": 6,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/564'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "agoric",
    "chainId": "agoric-3",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://atomscan.com/agoric",
      "txPath": "/transactions/",
      "accountPath": "/accounts/",
      "sampleTx": "576224B1A0F3D56BA23C5350C2A0E3CEA86F40005B828793E5ACBC2F4813152E",
      "sampleAccount": "agoric1cqvwa8jr6pmt45jndanc8lqmdsxjkhw0yertc0"
    },
    "info": {
      "url": "https://agoric.com",
      "source": "https://github.com/Agoric/agoric-sdk",
      "rpc": "https://agoric-rpc.polkachu.com",
      "documentation": "https://docs.agoric.com"
    }
  },
  {
    "id": "dydx",
    "name": "Dydx",
    "displayName": "dYdX",
    "coinId": 22000118,
    "symbol": "DYDX",
    "decimals": 18,
    "blockchain": "Cosmos",
    "derivation": [
      {
        "path": "m/44'/118'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1",
    "hrp": "dydx",
    "chainId": "dydx-mainnet-1",
    "addressHasher": "sha256ripemd",
    "explorer": {
      "url": "https://www.mintscan.io/dydx",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "F236222E4F7C92FA84711FD6451ED22DD56CBDFA319BFDAFB99A21E4E9B9EC2F",
      "sampleAccount": "dydx1adl7usw7z2dnysyn7wvrghu0u0q6gr7jqs4gtt"
    },
    "info": {
      "url": "https://dydx.exchange",
      "source": "https://github.com/dydxprotocol",
      "rpc": "https://dydx-dao-api.polkachu.com",
      "documentation": "https://docs.dydx.exchange"
    }
  },
  {
    "id": "nativeinjective",
    "name": "NativeInjective",
    "displayName": "Native Injective",
    "coinId": 10000060,
    "symbol": "INJ",
    "decimals": 18,
    "blockchain": "NativeInjective",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "inj",
    "addressHasher": "keccak256",
    "chainId": "injective-1",
    "explorer": {
      "url": "https://www.mintscan.io/injective",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "C5F6A4FF9DF1AE9FF543D2CEBD8E3E9B04290B2445F9D91D7707EDBF4B7EE16B",
      "sampleAccount": "inj1xmpkmxr4as00em23tc2zgmuyy2gr4h3wgcl6vd"
    },
    "info": {
      "url": "https://injective.com",
      "documentation": "https://docs.injective.network"
    }
  },
  {
    "id": "nativecanto",
    "name": "NativeCanto",
    "displayName": "NativeCanto",
    "coinId": 10007700,
    "symbol": "CANTO",
    "decimals": 18,
    "blockchain": "Cosmos",
    "chainId": "canto_7700-1",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "canto",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://mintscan.io/canto",
      "txPath": "/txs/",
      "accountPath": "/account/",
      "sampleTx": "7A7830270097AA9AC8B819EFBB8E0B56579F20ECB7615ECD37E19ABEEFB8DB83",
      "sampleAccount": "canto17xpfvakm2amg962yls6f84z3kell8c5lz0zsl4"
    },
    "info": {
      "url": "https://canto.io/",
      "documentation": "https://docs.canto.io/"
    }
  },
  {
    "id": "zetachain",
    "name": "NativeZetaChain",
    "displayName": "NativeZetaChain",
    "coinId": 10007000,
    "symbol": "ZETA",
    "decimals": 18,
    "blockchain": "Cosmos",
    "chainId": "zetachain_7000-1",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "hrp": "zeta",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.zetachain.com",
      "txPath": "/cosmos/tx/",
      "accountPath": "/address/",
      "sampleTx": "2DBB071DDD47985F4470A21E5943CE95D371AE4BDE2267E201D3553FB2BDCFDE",
      "sampleAccount": "zeta14py36sx57ud82t9yrks9z6hdsrpn5x6kmxs0ne"
    },
    "info": {
      "url": "https://www.zetachain.com/",
      "documentation": "https://www.zetachain.com/docs/"
    }
  },
  {
    "id": "zetaevm",
    "name": "Zeta EVM",
    "coinId": 20007000,
    "symbol": "ZETA",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "7000",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.zetachain.com",
      "txPath": "/evm/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x04cb1201857de29af97b755e51c888454fb96c1f3bb3c1329bb94d5353d5c19e",
      "sampleAccount": "0x85539A58F9c88DdDccBaBBfc660968323Fd1e167"
    },
    "info": {
      "url": "https://www.zetachain.com/",
      "documentation": "https://www.zetachain.com/docs/"
    }
  },
  {
    "id": "ton",
    "name": "TON",
    "coinId": 607,
    "symbol": "TON",
    "decimals": 9,
    "blockchain": "TheOpenNetwork",
    "derivation": [
      {
        "path": "m/44'/607'/0'"
      }
    ],
    "curve": "ed25519",
    "publicKeyType": "ed25519",
    "explorer": {
      "url": "https://tonviewer.com",
      "txPath": "/transaction/",
      "accountPath": "/",
      "sampleTx": "fJXfn0EVhV09HFuEgUHu4Cchb24nUQtIMwSzmzk2tLs=",
      "sampleAccount": "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"
    },
    "info": {
      "url": "https://ton.org",
      "source": "https://github.com/ton-blockchain",
      "rpc": "https://toncenter.com/api/v2/jsonRPC",
      "documentation": "https://ton.org/docs"
    }
  },
  {
    "id": "neon",
    "name": "Neon",
    "coinId": 245022934,
    "symbol": "NEON",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "245022934",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://neonscan.org",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x77d86af2c6f02f14ef13ca52bf54864d92fcc4b32d8e884e225061c006738ed6",
      "sampleAccount": "0xfa4a8650e7bebb918859c280a86f9661bed29877"
    },
    "info": {
      "url": "https://neonevm.org",
      "source": "https://github.com/neonevm/neon-evm",
      "rpc": "https://neon-proxy-mainnet.solana.p2p.org/",
      "documentation": "https://docs.neonfoundation.io/docs/quick_start"
    }
  },
  {
    "id": "internet_computer",
    "name": "Internet Computer",
    "coinId": 223,
    "symbol": "ICP",
    "decimals": 8,
    "blockchain": "InternetComputer",
    "derivation": [
      {
        "path": "m/44'/223'/0'/0/0",
        "xpub": "xpub",
        "xpriv": "xpriv"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "explorer": {
      "url": "https://dashboard.internetcomputer.org",
      "txPath": "/transaction/",
      "accountPath": "/account/",
      "sampleTx": "9e32c54975adf84a1d98f19df41bbc34a752a899c32cc9c0000200b2c4308f85",
      "sampleAccount": "529ea51c22e8d66e8302eabd9297b100fdb369109822248bb86939a671fbc55b"
    },
    "info": {
      "url": "https://internetcomputer.org",
      "source": "https://github.com/dfinity/ic",
      "rpc": "",
      "documentation": "https://internetcomputer.org/docs"
    }
  },
  {
    "id": "manta",
    "name": "Manta Pacific",
    "coinId": 169,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "169",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://pacific-explorer.manta.network",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x2bbd5d85b0ed05d1416e30ce1197a6f0c27d10ce02593a2719e2baf486d2e8c2",
      "sampleAccount": "0xF122a1aC569a36a5Cf6d0F828A22254c8A9afF84"
    },
    "info": {
      "url": "https://pacific.manta.network",
      "source": "https://github.com/manta-network",
      "rpc": "https://pacific-rpc.manta.network/http",
      "documentation": "https://docs.manta.network/docs/Introduction"
    }
  },
  {
    "id": "merlin",
    "name": "Merlin",
    "coinId": 4200,
    "symbol": "BTC",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "4200",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://scan.merlinchain.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xca6f2891959b669237738dd0bc2c1051d966778c9de90b94165032ce58364212",
      "sampleAccount": "0xf7e017b3f61bD3410A3b03D7DAD7699FD6780584"
    },
    "info": {
      "url": "https://merlinchain.io",
      "source": "https://merlinchain.io",
      "rpc": "https://rpc.merlinchain.io",
      "documentation": "https://docs.merlinchain.io/merlin-docs"
    }
  },
  {
    "id": "lightlink",
    "name": "Lightlink",
    "displayName": "Lightlink Phoenix",
    "coinId": 1890,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "1890",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://phoenix.lightlink.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xc65f82445aefc883fd4ffe09149c8ce48f61b670c0734528a49d4a8bd8309bb0",
      "sampleAccount": "0x4566ED6c7a7fFc90E2C7cfF7eB9156262afD2fDe"
    },
    "info": {
      "url": "https://lightlink.io",
      "source": "https://github.com/lightlink-network",
      "rpc": "https://endpoints.omniatech.io/v1/lightlink/phoenix/public",
      "documentation": "https://docs.lightlink.io/lightlink-protocol"
    }
  },
  {
    "id": "blast",
    "name": "Blast",
    "coinId": 81457,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "81457",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://blastscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x511fc00e8329343b9e953bf1f75e9b0a7b3cc2eb3a8f049d5be41adf4fbd6cac",
      "sampleAccount": "0x0d11f2f0ff55c4fcfc3ff86bdc8e78ffa7df99fd"
    },
    "info": {
      "url": "https://blast.io",
      "source": "https://github.com/blast-io",
      "rpc": "https://rpc.blast.io",
      "documentation": "https://docs.blast.io"
    }
  },
  {
    "id": "bouncebit",
    "name": "BounceBit",
    "coinId": 6001,
    "symbol": "BB",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "6001",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://bbscan.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0x52558f4143d058d942e3b73414090266ae3ffce1fe8c25fe86896e2c8e5ef932",
      "sampleAccount": "0xf4aa7349a9ccca4609943955b5ddc7bd9278c223"
    },
    "info": {
      "url": "https://bouncebit.io",
      "source": "https://github.com/BounceBit-Labs",
      "rpc": "https://fullnode-mainnet.bouncebitapi.com",
      "documentation": "https://docs.bouncebit.io"
    }
  },
  {
    "id": "zklinknova",
    "name": "ZkLinkNova",
    "displayName": "zkLink Nova Mainnet",
    "coinId": 810180,
    "symbol": "ETH",
    "decimals": 18,
    "blockchain": "Ethereum",
    "derivation": [
      {
        "path": "m/44'/60'/0'/0/0"
      }
    ],
    "curve": "secp256k1",
    "publicKeyType": "secp256k1Extended",
    "chainId": "810180",
    "addressHasher": "keccak256",
    "explorer": {
      "url": "https://explorer.zklink.io",
      "txPath": "/tx/",
      "accountPath": "/address/",
      "sampleTx": "0xeb5eb8710369c89115a83f3e744c15c9d388030cfce2fd3a653dbd18f2947400",
      "sampleAccount": "0xF95115BaD9a4585B3C5e2bfB50579f17163A45aA"
    },
    "info": {
      "url": "https://zklink.io",
      "source": "https://github.com/zkLinkProtocol",
      "rpc": "https://rpc.zklink.io",
      "documentation": "https://docs.zklink.io"
    }
  }
]

def find(li):
    for i in range(0,len(l)):
        if l[i]['id'] == "usdt":
            print(l[i])
find(l)