const state = {
  gender: 'random',
  surnameType: 'single',
  givenType: 'double'
};

const apiBase = 'http://127.0.0.1:5000';
const resultEl = document.getElementById('nameResult');
const generateBtn = document.getElementById('generateBtn');

document.querySelectorAll('.choice').forEach((btn) => {
  btn.addEventListener('click', () => {
    const key = btn.dataset.key;
    const value = btn.dataset.value;
    state[key] = value;

    document.querySelectorAll('.choice[data-key=' + key + ']').forEach((node) => {
      node.classList.remove('active');
    });
    btn.classList.add('active');
  });
});

generateBtn.addEventListener('click', async () => {
  generateBtn.disabled = true;
  resultEl.textContent = '...';

  try {
    const params = new URLSearchParams(state);
    const res = await fetch(apiBase + '/api/generate?' + params.toString());
    if (!res.ok) throw new Error('request failed: ' + res.status);

    const data = await res.json();
    resultEl.textContent = data.name;
  } catch (err) {
    resultEl.textContent = 'Generate failed';
    console.error(err);
  } finally {
    generateBtn.disabled = false;
  }
});
