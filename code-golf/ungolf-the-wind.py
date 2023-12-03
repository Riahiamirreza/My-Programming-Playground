# https://codegolf.stackexchange.com/questions/267235/ungolf-the-wind 


f = lambda s: ((-1 if (direction:=(s:=s.split()[3])[:3]) == 'VRB' else direction), s[3:5], s[(i:=s.index('G'))+1:i+3] if 'G' in s else -1)

assert f(
        "METAR KPDX 241653Z 16003KT 1/4SM R10R/4500VP6000FT FG SCT000 01/M01 A3040 RMK AO2 SLP293 FG SCT000 T00061006"
) == ("160", "03", -1)
