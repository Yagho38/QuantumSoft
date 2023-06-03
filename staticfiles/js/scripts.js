
// Menu Mobile

document.getElementById("hamburguer-icon").onclick = function () {

  document.getElementById("sliding-header-menu-outer").style.right = "0";

};

document.getElementById("sliding-header-menu-close-button").onclick = function () {

  document.getElementById("sliding-header-menu-outer").style.right = "-320px";

};


// About us Tab

var aboutUs = {
  "Missão": "Levar para nossos clientes soluções de tecnologia de alta qualidade que aumentam a eficiência e produtividade dos negócios e contribuam para o sucesso dos negócios.",
  "Visão": "Ser reconhecido como excelência na prestação de serviços de Tecnologia da Informação e Comunicação por nossos usuários. Ser para nossos clientes, como um Porto Seguro sempre gerando confiança e segurança para os nossos clientes.",
  "Valores": "<ul><li>Qualidade</li><li>Transparência</li><li>Ética</li><li>Colaboração</li><li>Flexibilidade</li><li>Excelência</li><li>Responsabilidade Social</li></ul>"
};

var unselected_color = "#646872";
var selected_color = "#2A2D34";

var about_tags = document.getElementsByClassName("single-tab");

for (var a = 0; a < about_tags.length; a++) {

  about_tags[a].onclick = function () {

    for (var b = 0; b < about_tags.length; b++) {
      about_tags[b].style['background-color'] = unselected_color;
      about_tags[b].style['font-weight'] = "normal";
    }

    this.style['background-color'] = selected_color;
    this.style['font-weight'] = "bold";

    var selecionado = this.innerHTML;

    document.getElementById("box-text").innerHTML = aboutUs[selecionado];

  };

  


}



// Slider de serviços

var our_services = [
  {
    'title': 'Webdesign',
    'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent finibus tincidunt sem non sodales. Nunc et quam in magna vehicula sollicitudin. Aliquam erat volutpat. Maecenas dolor mi, aliquet ac quam aliquet, condimentum dictum nisi.'
  },

  {
    'title': 'Branding',
    'text': 'Praesent finibus tincidunt sem non sodales. Nunc et quam in magna vehicula sollicitudin. Aliquam erat volutpat. Maecenas dolor mi, aliquet ac quam aliquet, condimentum dictum nisi.'
  },

  {
    'title': 'Marketing Digital',
    'text': 'Nunc et quam in magna vehicula sollicitudin. Aliquam erat volutpat. Maecenas dolor mi, aliquet ac quam aliquet, condimentum dictum nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent finibus.'
  }
  
];

// service-previous
// service-next
// service-title
// service-text

var servico_atual = 0;

document.getElementById("service-previous").onclick = function() {

  if (servico_atual == 0) {
    var servico_anterior = our_services.length - 1;
  } else {
    var servico_anterior = servico_atual - 1;
  }

  document.getElementById("service-title").innerHTML = our_services[servico_anterior].title;
  document.getElementById("service-text").innerHTML = our_services[servico_anterior].text;
  servico_atual = servico_anterior;

};

document.getElementById("service-next").onclick = function() {

  if (servico_atual == our_services.length - 1) {
    var servico_seguinte = 0;
  } else {
    var servico_seguinte = servico_atual + 1;
  }

  document.getElementById("service-title").innerHTML = our_services[servico_seguinte].title;
  document.getElementById("service-text").innerHTML = our_services[servico_seguinte].text;
  servico_atual = servico_seguinte;


};

// Data Footer

var ano_atual = new Date;
ano_atual = ano_atual.getFullYear();
document.getElementById("current_year").innerHTML = ano_atual;


// API Key Google: AIzaSyBMD-clZ1JUApCv7BN6JH3b6RN2hd62hz8

  
   


   