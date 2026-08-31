class SiteFooter extends HTMLElement {
  async connectedCallback() {
    const res = await fetch("/includes/site-footer.html");
    if (!res.ok) return;
    const html = await res.text();
    const tpl = document.createElement("template");
    tpl.innerHTML = html;
    this.replaceWith(tpl.content.cloneNode(true));
  }
}
customElements.define("site-footer", SiteFooter);
