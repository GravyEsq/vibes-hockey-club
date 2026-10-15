/* Respect the device theme until the reader explicitly chooses Light or Dark. */
(()=>{
  const root=document.documentElement;
  const select=document.getElementById('theme-select');
  const device=window.matchMedia('(prefers-color-scheme: dark)');
  let preference=root.dataset.themePreference||'system';
  function apply(){
    const dark=preference==='dark'||(preference==='system'&&device.matches);
    root.dataset.theme=dark?'dark':'light';
    root.dataset.themePreference=preference;
    document.querySelector('meta[name="theme-color"]').content=dark?'#10191f':'#f4f1e9';
    select.value=preference;
  }
  select.addEventListener('change',()=>{
    preference=select.value;
    try{localStorage.setItem('vhc-theme',JSON.stringify(preference))}catch{}
    apply();
  });
  device.addEventListener('change',()=>{if(preference==='system')apply()});
  apply();
})();
