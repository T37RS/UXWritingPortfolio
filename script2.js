function addReminder() {
    const reminderInput = document.getElementById('reminder-input');
    const reminderList = document.getElementById('reminder-list');

    const reminderText = reminderInput.value.trim();
    if (reminderText !== '') {
        const reminderItem = document.createElement('div');
        reminderItem.classList.add('reminder-item');
        reminderItem.innerText = reminderText;
        reminderList.appendChild(reminderItem);

        // Clear the input
        reminderInput.value = '';
    }
}