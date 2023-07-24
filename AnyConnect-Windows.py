�
    [z�d�  �                   �&  � d dl Z d dlZd dlZd dlmZ g ZdZdZ e j        e�  �        D ]�Z	e	�
                    d�  �        s�e j        �                    ee	�  �        Z eed�  �        5 Ze�                    �   �         Z eed�  �        Ze�                    d�  �        j        Ze�                    e�  �         ddd�  �         n# 1 swxY w Y   �� ej        d	d
d� eD �   �         ��  �        gZ ej        e�  �        Zed	         Z ej        d	dg d���  �        gZ ej        e�  �        Zed	         Zedk    r ej        ededg�  �         dS edk    r ej        edeg�  �         dS edk    r ej        edeg�  �         dS  ed�  �         dS )�    N)�BeautifulSoupzDc:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\ProfilezOc:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exez.xml�r�xml�HostName�ConnectionTypezSelect a connection:c                 �   � g | ]}|��S � r	   )�.0�
connections     �AnyConnect-Windows.py�
<listcomp>r   &   s   � �Q�Q�Q�
��Q�Q�Q�    )�message�choiceszSelect an action:)�connect�
disconnect�statusr   z-sr   r   z<The action choice selected doesn't exist. Contact developer.)�os�inquirer�
subprocess�bs4r   �ListOfAvailableConnections�AnyConnectProfilesPath�AnyConnectVpnCli�listdir�filename�endswith�path�join�fullname�open�f�read�data�Bs_data�find�string�Hostname�append�List�	questions�prompt�answers�answer�run�printr	   r   r   �<module>r1      s�  �� 
�	�	�	� ���� � � � � � � � � � �  � �_� �h� � ��
�1�2�2� 4� 4�H����V�$�$�.�h��w�|�|�2�H�=�=�H� 
��h��	�	� 	4���v�v�x�x���-��e�,�,���<�<�
�+�+�2�� 	#�)�)�(�3�3�3�	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4���� 	4� 	4� 	4� 	4�� �H�M�"�.�Q�Q�6P�Q�Q�Q�� � ��	� �(�/�)�
$�
$��	�!�	"�� �H�M�"�+�;�;�;�� � ��	� �(�/�)�
$�
$��	�!�	"��	�Y����J�N�$�j�&�%�@�A�A�A�A�A��|����J�N�$�m�V�<�=�=�=�=�=��x����J�N�$�i��8�9�9�9�9�9� 
�E�
H�I�I�I�I�Is   �(AC�C	�C	