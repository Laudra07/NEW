import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))