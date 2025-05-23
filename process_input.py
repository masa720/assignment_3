import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

original_x = x

x += y
step1 = x

x -= z
step2 = x

x *= y
step3 = x

x %= z
step4 = x

x /= z
step5 = x

final_result = step5 + y + z

print(f"""
<html>
<body>
    <div style="background-color:#fde7d8; border:1px solid black; padding:15px; width:500px;">
        <h1>Assignment #3</h1>
        <p>Python Script Result<br>Original Values:</p>
        <ul>
            <li><strong>x:</strong> {original_x}</li>
            <li><strong>y:</strong> {y}</li>
            <li><strong>z:</strong> {z}</li>
        </ul>
    </div>
    <h3>Calculation Steps:</h3>
    <ul>
        <li>Initial value of x: <strong>{original_x}</strong></li>
        <li>After x += y: <strong>{step1}</strong></li>
        <li>After x -= z: <strong>{step2}</strong></li>
        <li>After x *= y: <strong>{step3}</strong></li>
        <li>After x %= z: <strong>{step4}</strong></li>
        <li>After x /= z: <strong>{step5}</strong></li>
    </ul>
    <p><strong>Final Result: x + y + z is: {step5} + {y} + {z} = {final_result}</strong></p>
</body>
</html>
""")
