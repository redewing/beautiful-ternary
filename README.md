# beautiful-ternary
A simple Python Package to replace the awkward built-in ternary operator with a function call. Simple.

# Usage

    pip install beautiful-ternary
    
    from ternary import tif, tlif
    
    # Use this for non-lazy ternary
    tif(condition, return-if-true, return-if-false)
    
    # Use this for lazy ternary
    tlif(condition, lambda: return-if-true, lambda: return-if-false)

# Dependencies

    build, twine, pytest
