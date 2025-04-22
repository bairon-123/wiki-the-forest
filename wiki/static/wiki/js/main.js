document.addEventListener('DOMContentLoaded', function () {
	const fila = document.querySelector('.carousel');
	const peliculas = document.querySelectorAll('.pelicula');
	const flechaIzquierda = document.querySelector('.flecha-izquierda');
	const flechaDerecha = document.querySelector('.flecha-derecha');

	if (!fila || !flechaIzquierda || !flechaDerecha) return;

	// Flecha derecha
	flechaDerecha.addEventListener('click', () => {
		fila.scrollLeft += fila.offsetWidth * 0.8;
		const indicadorActivo = document.querySelector('.indicadores .activo');
		if (indicadorActivo?.nextElementSibling) {
			indicadorActivo.classList.remove('activo');
			indicadorActivo.nextElementSibling.classList.add('activo');
		}
	});

	// Flecha izquierda
	flechaIzquierda.addEventListener('click', () => {
		fila.scrollLeft -= fila.offsetWidth * 0.8;
		const indicadorActivo = document.querySelector('.indicadores .activo');
		if (indicadorActivo?.previousElementSibling) {
			indicadorActivo.classList.remove('activo');
			indicadorActivo.previousElementSibling.classList.add('activo');
		}
	});

	// Paginación
	const numeroPaginas = Math.ceil(peliculas.length / 4);
	const indicadores = document.querySelector('.indicadores');
	for (let i = 0; i < numeroPaginas; i++) {
		const indicador = document.createElement('button');
		if (i === 0) indicador.classList.add('activo');

		indicador.addEventListener('click', (e) => {
			fila.scrollLeft = i * fila.offsetWidth;
			document.querySelector('.indicadores .activo').classList.remove('activo');
			e.target.classList.add('activo');
		});
		indicadores.appendChild(indicador);
	}

	// Hover
	peliculas.forEach((pelicula) => {
		pelicula.addEventListener('mouseenter', (e) => {
			const elemento = e.currentTarget;
			setTimeout(() => {
				peliculas.forEach(p => p.classList.remove('hover'));
				elemento.classList.add('hover');
			}, 300);
		});
	});

	fila.addEventListener('mouseleave', () => {
		peliculas.forEach(p => p.classList.remove('hover'));
	});
});