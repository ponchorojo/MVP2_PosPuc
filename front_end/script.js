document.getElementById("formulario").addEventListener("submit", async function (e) {
    e.preventDefault();

    const dados = {
        ApplicantIncome: parseFloat(document.getElementById("ApplicantIncome").value),
        CoapplicantIncome: parseFloat(document.getElementById("CoapplicantIncome").value),
        LoanAmount: parseFloat(document.getElementById("LoanAmount").value),
        Loan_Amount_Term: parseFloat(document.getElementById("Loan_Amount_Term").value),
        Credit_History: parseInt(document.getElementById("Credit_History").value),
    };

    const res = await fetch("http://localhost:5000/prever", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
    });

    const json = await res.json();
    document.getElementById("resultado").innerText = "Resultado: " + json.resultado;
});
