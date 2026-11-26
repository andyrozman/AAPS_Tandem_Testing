// The old documentation was a single index.html page. Existing links such as
// .../AAPS_Tandem_Testing/#connection-setup point at sections that now live on
// their own pages. Redirect those old anchors to the new location.
(function () {
  var map = {
    "t-mobi-documentation": "index.html",
    "powering-on-mobi": "CompatiblePumps/TandemMobi.html#tandem-mobi-power-on",
    "connection-setup": "CompatiblePumps/TandemMobi.html#tandem-mobi-setup",
    "a-using-shared-connection": "CompatiblePumps/TandemMobi.html#tandem-mobi-pair-controlx2",
    "b-using-only-aaps": "CompatiblePumps/TandemMobi.html#tandem-mobi-pair-aaps",
    "overview": "CompatiblePumps/TandemMobi.html#tandem-mobi-pump-screen",
    "configuration-options": "CompatiblePumps/TandemMobi.html#tandem-mobi-settings",
    "mobi-details": "CompatiblePumps/TandemMobi.html#tandem-mobi-architecture",
    "mobi-details-limitations": "CompatiblePumps/TandemMobi.html#tandem-mobi-limitations",
    "mobi-details-startup-sequence": "CompatiblePumps/TandemMobi.html#tandem-mobi-startup-sequence",
    "mobi-details-pump-notifications": "CompatiblePumps/TandemMobi.html#tandem-mobi-notifications-explained",
    "mobi-details-events": "CompatiblePumps/TandemMobi.html#tandem-mobi-events",
    "mobi-details-pump-refresh": "CompatiblePumps/TandemMobi.html#tandem-mobi-refresh-schedule",
    "mobi-details-bolus": "CompatiblePumps/TandemMobi.html#tandem-mobi-bolus-progress",
    "actions": "CompatiblePumps/TandemMobi.html#tandem-mobi-actions",
    "actions-refresh": "CompatiblePumps/TandemMobi.html#tandem-mobi-pump-screen",
    "data-button": "CompatiblePumps/TandemMobi.html#tandem-mobi-pump-data",
    "data-notifiction": "CompatiblePumps/TandemMobi.html#tandem-mobi-notifications",
    "data-events": "CompatiblePumps/TandemMobi.html#tandem-mobi-events-view",
    "data-history": "CompatiblePumps/TandemMobi.html#tandem-mobi-pump-history",
    "settings-button": "CompatiblePumps/TandemMobi.html#tandem-mobi-actions",
    "currently-implemented-functionalities": "CompatiblePumps/TandemMobi.html#tandem-mobi-capabilities",
    "troubleshooting": "CompatiblePumps/TandemMobi.html#tandem-mobi-troubleshooting"
  };
  function redirect() {
    var hash = window.location.hash.replace(/^#/, "");
    if (!hash || !map[hash]) return;
    // Only redirect from the site root / index page.
    var path = window.location.pathname;
    if (!/(\/|index\.html)$/.test(path)) return;
    if (document.getElementById(hash)) return; // anchor exists on this page
    var base = path.replace(/index\.html$/, "");
    window.location.replace(base + map[hash]);
  }
  // On load (a link from elsewhere), and when only the hash changes
  // (an old link followed while already on the home page).
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", redirect);
  } else {
    redirect();
  }
  window.addEventListener("hashchange", redirect);
})();
