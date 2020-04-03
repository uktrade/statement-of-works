import React from "react";
import { Link } from "react-router-dom";

import TopNav, { asNavLinkAnchor } from "@govuk-react/top-nav";

const NavAnchor = asNavLinkAnchor(Link);

const ServiceTitle = (
    <NavAnchor to="/">
        Statement of Works
    </NavAnchor>
);

const PageHeader = () => (
    <div>
        <TopNav company="" serviceTitle={ServiceTitle} />
    </div>
);

export default PageHeader;
