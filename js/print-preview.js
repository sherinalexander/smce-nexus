function printPreview(msg) {
    var printContent = document.querySelector('.printable-content');
    var newWindow = window.open('', '_blank');
    newWindow.document.write('<html><head><title>Print Preview</title></head><body>');
    newWindow.document.write(printContent.innerHTML);
    newWindow.document.write('</body></html>');
    newWindow.document.close();
    newWindow.print();
    newWindow.document.close();
}
