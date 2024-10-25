# BlenderTextAsset

export mesh data to a `text.bin`

## bin format

### Header

description                     | format (python)
------------------------------- | -------------
number of letters               | uint8_t (B) 
total letters mesh data size    | uint32_t (I)
letters                         | [letter](#letter)

## Letter

description                     | format (python)
------------------------------- | -------------
letter itself ('A')             | uint8_t (B)
letter mesh data size           | uint32_t (I)
mesha data itself               | float (f) (default 3 floats per vertex)
