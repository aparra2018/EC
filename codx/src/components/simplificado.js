
import React from 'react'
import { Nav, NavItem, Button, NavbarText, Input} from 'reactstrap';
import {ConseguirArchivo, PostDatos,TablaFrecuenciasDesdeArchivo, GraficarDesdeArchivo, ObtenerDatosMapa} from './consultas';
import './comps.css';
import {Menu,MenuItem } from '@szhsin/react-menu';
import '@szhsin/react-menu/dist/index.css';

export const Sim = (props) => {
  return (
    <div id="Simplificado">
      <Nav>
        <NavItem>
          <NavbarText>Manejo BD</NavbarText>
            <div className="btn-group btn-sm">
            <Menu className=" bg-info text-white border border-primary" menuButton={
              <button className="btn btn-primary" >Consultas</button>}>
                <MenuItem className="bg-info" onClick={()=>ConseguirArchivo(props,"1")}>Archivo JSON</MenuItem>
            </Menu>
            <Button color="info" onClick={()=>PostDatos(props.env)}>Actualizar</Button>
            </div>
        </NavItem>
        <NavItem>
         <NavbarText>Consulta por ID</NavbarText> 
         <div className="input-group input-group-sm">
            <div className="col-auto">
              <Input type="text" className="form-control bg-dark border border-primary text-white" id="ID"></Input>
            </div>
          </div>
          <div className="btn-group btn-sm">
            <Button color="success" onClick={()=>ConseguirArchivo(props,document.getElementById("ID").value)}>Buscar</Button>
          </div>
        </NavItem>
      <NavItem>
            <Button color="primary" onClick={()=>GraficarDesdeArchivo(props.setGrafico,props.env,props.camps)}>Graficar Desde Archivo</Button>
            <Button color="primary" onClick={()=>TablaFrecuenciasDesdeArchivo(props.setEstadigrafo,props.env,props.camps)}>Tabla de Frecuencias</Button>
            <Button color="primary" onClick={()=>ObtenerDatosMapa(props.setUbicacion,props.env,props.camps)}>Mostrar en Mapa</Button>
        </NavItem>
      </Nav>
    </div>
  );
}
