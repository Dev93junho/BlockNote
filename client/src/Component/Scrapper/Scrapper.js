import React from "react";
import Styled from 'styled-components';

const ScrapSidebar = Styled.div`
position: fixed;
width: 120px;
height: 400px;
left: 70%;
`

const InputUrl = Styled.form`
width: 100px;
height: 55px;
`

export default function Scrapper () {
    return (
        <ScrapSidebar>
            {/* before : btn-menu , after : full-menu */}
            <div className="CtrlSize">1</div>
            <div className="InputUrl-sm">
                <InputUrl  methods={['GET']}>
                    <input type="url" name="url" placeholder="plz input url" />
                    <button type="submit">enter</button>
                </InputUrl>
            </div>
            <div className="TbStore">2</div>
            <div className="StrStore">3</div>
        </ ScrapSidebar>
    )
}