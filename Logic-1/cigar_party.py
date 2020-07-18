def cigar_party(cigars, is_weekend):
  return((cigars>=40 and cigars<=60 and not is_weekend) 
  or (cigars>=40 and is_weekend))


print(cigar_party(30, False) )
print(cigar_party(50, False))
print(cigar_party(70, True) )