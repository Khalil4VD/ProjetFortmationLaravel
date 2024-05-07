@extends('Layout.Liverpool')

@section('content')

@section('content')
<h1>Liste des joueurs</h1>
@if($posts->count() > 0)
    <ol>
    @foreach($posts as $post)
        <li><a href="{{ route('RouteJoueur', ['id' => $post->id]) }}">{{ $post->title }}</a></li>
    @endforeach
    </ol>
@else
    <span>Aucun joueur disponible actuellement</span>
@endif

@endsection

@endsection
