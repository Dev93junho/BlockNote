const jsPDF = require('jspdf');
const docx = require('docx');
const { saveAs } = require('file-saver');

// Toggle the sidebar
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const main = document.getElementById('main');
  if (sidebar.style.left === '-250px') {
    sidebar.style.left = '0';
    main.style.marginLeft = '250px';
  } else {
    sidebar.style.left = '-250px';
    main.style.marginLeft = '0';
  }
}

// Save the text as a docx or pdf file
function saveText() {
  // Get the text from the editor
  const text = document.getElementById('editor').innerHTML;

  // Save the text to local storage
  localStorage.setItem('text', text);

  // Create a new docx document
  const doc = new docx.Document();
  doc.addSection({
    children: [
      new docx.Paragraph(text),
    ],
  });

  // Convert the document to a buffer
  const docxBuffer = docx.Packer.toBuffer(doc);

  // Save the text as a docx file
  const docxBlob = new Blob([docxBuffer], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
  saveAs(docxBlob, 'document.docx');

  // Convert the text to a pdf file
  const pdf = new jsPDF();
  pdf.text(text, 10, 10);
  pdf.save('document.pdf');

  alert('Text saved successfully!');
}

// Clear the editor
function clearText() {
  document.getElementById('editor').innerHTML = '';
  alert('Editor cleared successfully!');
}

// Load the saved text on page load
window.onload = function () {
  const savedText = localStorage.getItem('text');
  if (savedText !== null) {
    document.getElementById('editor').innerHTML = savedText;
  }
};
