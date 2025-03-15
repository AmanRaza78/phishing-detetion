chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    let url = tabs[0].url;
    fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = data.phishing 
            ? "⚠️ Phishing Site Detected!" 
            : "✔️ Safe Site";
    })
    .catch(error => console.error("Error:", error));
});
