<ul class="navbar">
    <li><a href="{{ route('welcome') }}">Page d'acceuil</a></li>
    <li><a href="{{ route('RouteCreate') }}">Ajouter un joueur de Liverpool ?</a></li>
    <li><a href="{{ route('contact') }}">Contact</a></li>
    <li>
    <a href="#" onclick="document.getElementById('logout-form').submit();">
        Se déconnecter
    </a>
    <form action="{{ route('logout') }}" method="post" id="logout-form" style="display: none;">
        @csrf <!-- Utilisez @csrf pour générer le jeton CSRF -->
    </form>
    </li>

</ul>