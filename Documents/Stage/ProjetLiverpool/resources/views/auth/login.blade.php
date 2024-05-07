@extends('Layout.Liverpool')



@section('content')
<h1 style="margin-left: 34%;">Connectez-vous :</h1>

@if ($errors->any())
@foreach ($errors->all() as $error)
<div class="erreur" style="background-color: #C8102E; margin-left:30%; margin-right:40%; color: #FFFFFF; padding: 10px;">
    {{$error}}
</div>

@endforeach
@endif


<form method="POST" action="{{ route('authenticate') }}" style="max-width: 400px; margin: 0 auto;">
    @csrf
    <label for="email">Adresse e-mail :</label><br>
    <input type="email" name="email"><br><br>

    <label for="password">Mot de passe :</label><br>
    <input type="password" name="password"><br><br>

    <button type="submit">Se connecter</button>
</form>


@endsection