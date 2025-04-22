const indicadorActivo = document.querySelector('.indicadores .activo');
if (indicadorActivo && indicadorActivo.previousElementSibling) {
	indicadorActivo.classList.remove('activo');
	indicadorActivo.previousElementSibling.classList.add('activo');
}

  if (!fila || peliculas.length === 0) return;

  flechaDerecha?.addEventListener('click', () => {
    fila.scrollLeft += fila.offsetWidth;
  });

  flechaIzquierda?.addEventListener('click', () => {
    fila.scrollLeft -= fila.offsetWidth;
  });

  // Indicadores
  const numeroPaginas = Math.ceil(peliculas.length / 4);
  const contenedorIndicadores = document.querySelector('.indicadores');

  for (let i = 0; i < numeroPaginas; i++) {
    const btn = document.createElement('button');
    if (i === 0) btn.classList.add('activo');
    contenedorIndicadores.appendChild(btn);

    btn.addEventListener('click', (e) => {
      fila.scrollLeft = i * fila.offsetWidth;
      document.querySelector('.indicadores .activo')?.classList.remove('activo');
      e.target.classList.add('activo');
    });
  }

  peliculas.forEach((pelicula) => {
    pelicula.addEventListener('mouseenter', () => {
      peliculas.forEach(p => p.classList.remove('hover'));
      pelicula.classList.add('hover');
    });
  });

  fila.addEventListener('mouseleave', () => {
    peliculas.forEach(p => p.classList.remove('hover'));
  });
  