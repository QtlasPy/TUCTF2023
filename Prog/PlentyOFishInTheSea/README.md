<h1> Plenty O Fish in the Sea : Easy </h1>

<p> On this one we have to find the "One Bit" in a map wich is a log file. So we can start by find numbers in this large text file : </p>

```bash
┌──(atlas💀Kali)-[Prog/PlentyOFishInTheSea]
└─$ grep -E "[0-9]" lost_map.log
%7B83h%2
1Nd_7h3_
W%4073rF
%4011%7D
```
<p> And we find these 3 expressions which seem to be encoded, and when we put them end to end to decode them we find the flag :  <strong> {83h!Nd_7h3_W@73rF@11} </strong></p>
