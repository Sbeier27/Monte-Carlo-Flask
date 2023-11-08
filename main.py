import random
from flask import Flask, request, render_template

app = Flask(__name__)

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    estimated_pi = (inside_circle / num_samples) * 4
    return estimated_pi

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_samples = int(request.form['num_samples'])
        estimated_pi = monte_carlo_pi(num_samples)
        return render_template('index.html', estimated_pi=estimated_pi)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


