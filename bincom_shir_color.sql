PGDMP     '    7                {            bincom    15.3    15.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    40974    bincom    DATABASE     �   CREATE DATABASE bincom WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE bincom;
                postgres    false            �            1259    49167    color    TABLE     #  CREATE TABLE public.color (
    id bigint NOT NULL,
    days character varying(50),
    green integer,
    yellow integer,
    blue integer,
    pink integer,
    orange integer,
    cream integer,
    red integer,
    white integer,
    brown integer,
    ash integer,
    black integer
);
    DROP TABLE public.color;
       public         heap    postgres    false            �            1259    49166    color_id_seq    SEQUENCE     u   CREATE SEQUENCE public.color_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.color_id_seq;
       public          postgres    false    215            �           0    0    color_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.color_id_seq OWNED BY public.color.id;
          public          postgres    false    214            e           2604    49170    color id    DEFAULT     d   ALTER TABLE ONLY public.color ALTER COLUMN id SET DEFAULT nextval('public.color_id_seq'::regclass);
 7   ALTER TABLE public.color ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            �          0    49167    color 
   TABLE DATA           r   COPY public.color (id, days, green, yellow, blue, pink, orange, cream, red, white, brown, ash, black) FROM stdin;
    public          postgres    false    215          �           0    0    color_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.color_id_seq', 5, true);
          public          postgres    false    214            g           2606    49172    color color_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.color
    ADD CONSTRAINT color_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.color DROP CONSTRAINT color_pkey;
       public            postgres    false    215            �   o   x�E�A
�0ϛ�im��/�EPу�"�ޤ�HBX6�c��8<�0�`����K��yM���deTp�P�,�i�ҭ��X����\��1,9�Տ8�i-��|�1����He$�     