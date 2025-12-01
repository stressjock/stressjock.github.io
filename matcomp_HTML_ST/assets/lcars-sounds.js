// lcars-sounds.js
// Helper JS for Streamlit + LCARS: exposes playLCARS() and attaches listeners to Streamlit controls.
// It expects audio elements with ids audio1, audio2, ... present in the page.

window.playLCARS = window.playLCARS || function(idx=1) {
  try {
    var id = "audio" + idx;
    var a = document.getElementById(id) || document.getElementById("lcars_audio_" + idx);
    if (a) {
      a.currentTime = 0;
      a.play();
    }
  } catch(e) {
    console.warn("playLCARS error:", e);
  }
};

// Attach mild click/tap play to newly added Streamlit buttons/selects
(function attachLCARSHook() {
  const playOnClick = (ev) => {
    // play first audio by default
    window.playLCARS(1);
  };
  const obs = new MutationObserver((mutationsList) => {
    try {
      document.querySelectorAll('button, [data-baseweb="select"]').forEach(el => {
        if (!el._lcars_hooked) {
          el.addEventListener('click', playOnClick);
          el._lcars_hooked = true;
        }
      });
    } catch(e) {}
  });
  obs.observe(document.body, { childList: true, subtree: true });
})();
