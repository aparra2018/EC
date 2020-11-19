import React from 'react'
import { Nav, NavItem, Button,Input } from 'reactstrap';
import {ConseguirArchivo, GraficarDesdeArchivo} from './consultas';
import './comps.css';
import '@szhsin/react-menu/dist/index.css';

export const Sim = (props) => {
  return (
    <div id="Simplificado">
      
      <Nav>
        <p>Manejo BD</p>
        <NavItem>
          <div className="input-group input-group-sm">
            <div className="col-auto">
              <Input type="text" className="form-control bg-dark border border-primary text-white" id="ID"></Input>
            </div>
          </div>
          <div className="btn-group btn-sm">
            <Button color="success" onClick={()=>ConseguirArchivo(props,document.getElementById("ID").value)}>Consulta</Button>
          </div>
        </NavItem>
      <hr />
        <NavItem>
          <Button color="primary" onClick={()=>GraficarDesdeArchivo(props.setImagen,props.env,props.camps)}>Graficar Desde Archivo</Button>
        </NavItem>
      </Nav>
    </div>
  );
}
