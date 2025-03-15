chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url) {
        fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: tab.url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.phishing) {
                chrome.action.setBadgeText({ text: "⚠️", tabId: tabId });
                chrome.action.setBadgeBackgroundColor({ color: "red" });
            } else {
                chrome.action.setBadgeText({ text: "✔️", tabId: tabId });
                chrome.action.setBadgeBackgroundColor({ color: "green" });
            }
        })
        .catch(error => console.error("Error detecting phishing:", error));
    }
});
