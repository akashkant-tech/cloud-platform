#!/usr/bin/python36

print("content-type: text/html")
print("")



print("""<form action="test.py">
    <label for="name">ContainerName:</label>
    <input type="text" id="name" name="cn"> 

    <label for="cimg">ContainerImage:</label>
    <select id="cimg" name="img">
      <option value="Centos">Centos</option>
      <option value="Ubuntu">Ubuntu</option>
    </select>  

    <input type="submit" value="submit">
  </form>""")
 
