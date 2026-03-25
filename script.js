async function predictLoan() {
    const box = document.getElementById("predictionBox");
    const content = box.querySelector(".result-content");

    // Show loading
    content.innerHTML = '<div class="spinner"></div><div class="result-text loading">Analyzing...</div>';
    box.className = "result-box loading";

    const data = {
        person_age: document.getElementById("person_age").value,
        person_gender: document.getElementById("person_gender").value,
        person_education: document.getElementById("person_education").value,
        person_income: document.getElementById("person_income").value,
        person_emp_exp: document.getElementById("person_emp_exp").value,
        person_home_ownership: document.getElementById("person_home_ownership").value,
        loan_amnt: document.getElementById("loan_amnt").value,
        loan_intent: document.getElementById("loan_intent").value,
        loan_int_rate: document.getElementById("loan_int_rate").value,
        loan_percent_income: document.getElementById("loan_percent_income").value,
        cb_person_cred_hist_length: document.getElementById("cb_person_cred_hist_length").value,
        credit_score: document.getElementById("credit_score").value,
        previous_loan_defaults_on_file: document.getElementById("previous_loan_defaults_on_file").value
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) {
            content.innerHTML = '<div class="result-icon"></div><div class="result-text">ERROR</div>';
            box.className = "result-box rejected";
            return;
        }

        const isApproved = result.prediction === "Approved";
        const icon = isApproved ? "✓" : "✗";
        content.innerHTML = `<div class="result-icon">${icon}</div><div class="result-text">${result.prediction.toUpperCase()}</div>`;
        box.className = isApproved ? "result-box approved" : "result-box rejected";

    } catch (error) {
        content.innerHTML = '<div class="result-icon"></div><div class="result-text">Error</div>';
        box.className = "result-box rejected";
    }
}