// Exemple d'ajout d'une animation au survol des produits
const produits = document.querySelectorAll('.produit');

produits.forEach(produit => {
    produit.addEventListener('mouseover', () => {
        produit.style.transform = 'scale(1.05)';
        produit.style.transition = 'transform 0.3s ease';
    });

    produit.addEventListener('mouseout', () => {
        produit.style.transform = 'scale(1)';
    });
});