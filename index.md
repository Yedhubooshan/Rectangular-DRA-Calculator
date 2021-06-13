## Download And Run the File

### Enter Permittivity, Permeability, Length in mm, Width in mm, Height in mm.
Output displayed in GHz.

![image](https://user-images.githubusercontent.com/52876597/121818594-c3b4ac80-cca5-11eb-97c7-60d566b30b29.png)

Code Snippet:

```
        c = (3 * pow(10,8))/(math.sqrt(float(permittivity1)*float(permeability1))*2)
        a = round((1000/float(length1)),2)
        b = round((1000/float(width1)),2)
        d = round((1000/float(height1)),2)

        e,f,g = round(pow(a,2)),round(pow(b,2)),round(pow(d,2))
        
        total111 = (1*e) + (1*f) + (1*g)
        total101 = (1*e) + (0*f) + (1*g)
        total011 = (0*e) + (1*f) + (1*g)
        total110 = (1*e) + (1*f) + (0*g)
        total010 = (0*e) + (1*f) + (0*g)
        total100 = (1*e) + (0*f) + (0*g)


        dimen111 = math.sqrt(total111)
        dimen101 = math.sqrt(total101)
        dimen011 = math.sqrt(total011)
        dimen110 = math.sqrt(total110)
        dimen010 = math.sqrt(total010)
        dimen100 = math.sqrt(total100)

        final111 = round((dimen111*c)/pow(10,9),2)
        final101 = round((dimen101*c)/pow(10,9),2)
        final011 = round((dimen011*c)/pow(10,9),2)
        final110 = round((dimen110*c)/pow(10,9),2)
        final010 = round((dimen010*c)/pow(10,9),2)
        final100 = round((dimen100*c)/pow(10,9),2)
```
Calculation Part of the program displayed. Created based on the principle of Rectangular Waveguide Model.
