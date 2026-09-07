#
# PySNMP MIB module IANA-GBOND-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IANA-GBOND-TC-MIB
# Source digest sha256:22dd0afde0bb64a33c6eae2f94c950e1787a539cef7f5ebc87de80bc15d6e4b8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaGBondTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 215))
ianaGBondTcMIB.setRevisions(('2013-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaGBondTcMIB.setRevisionsDescriptions(('Initial version, published as RFC 6765.',))
if mibBuilder.loadTexts: ianaGBondTcMIB.setLastUpdated('2017-06-23 00:00')
if mibBuilder.loadTexts: ianaGBondTcMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaGBondTcMIB.setContactInfo('        Internet Assigned Numbers Authority\n\n                    Postal: ICANN\n                            12025 Waterfront Drive, Suite 300\n                            Los Angeles, CA 90094-2536\n\n                        Tel: +1-310-301-5800\n                      EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaGBondTcMIB.setDescription("This MIB module defines IANAgBondScheme and IANAgBondSchemeList\n        TEXTUAL-CONVENTIONs, specifying enumerated values of the\n        gBondPortConfAdminScheme, gBondPortConfPeerAdminScheme,\n        gBondPortStatOperScheme, gBondPortStatPeerOperScheme,\n        gBondPortCapSchemesSupported, and gBondPortCapPeerSchemesSupported\n        objects, respectively, as defined in the GBOND-MIB.\n\n        It is intended that each new bonding scheme defined by the\n        ITU-T Q4/SG15 working group and approved for publication in a\n        revision of the ITU-T G.998 specification will be added to this\n        MIB module, provided that it is suitable for being managed by the\n        base objects in the GBOND-MIB.  An Expert Review, as defined in\n        RFC 8126, is REQUIRED for such additions.\n\n        The following references are used throughout this MIB module:\n\n        [G.998.1] refers to:\n          ITU-T Recommendation G.998.1: 'ATM-based multi-pair bonding',\n          January 2005.\n\n        [G.998.2] refers to:\n          ITU-T Recommendation G.998.2: 'Ethernet-based multi-pair\n          bonding', January 2005.\n\n        [G.998.3] refers to:\n          ITU-T Recommendation G.998.3: 'Multi-pair bonding using\n          time-division inverse multiplexing', January 2005.\n\n        Naming Conventions:\n          BCE   - Bonding Channel Entity\n          GBS   - Generic Bonding Sub-layer\n\n        These references should be updated as appropriate when a new\n        bonding scheme is added to this MIB module.\n\n        Copyright (c) 2013 IETF Trust and the persons identified as\n        authors of the code.  All rights reserved.\n\n        Redistribution and use in source and binary forms, with or without\n        modification, is permitted pursuant to, and subject to the license\n        terms contained in, the Simplified BSD License set forth in\n        Section 4.c of the IETF Trust's Legal Provisions Relating to IETF\n        Documents (http://trustee.ietf.org/license-info).")
class IANAgBondSchemeList(TextualConvention, Bits):
    description = 'This textual convention defines a bitmap of possible ITU-T\n        G.998 (G.Bond) bonding schemes.  Currently, the following values\n        are defined for the corresponding bonding schemes:\n          g9981(1) - G.998.1 (G.Bond/ATM; see the G9981-MIB)\n          g9982(2) - G.998.2 (G.Bond/Ethernet; see the G9982-MIB)\n          g9983(3) - G.998.3 (G.Bond/TDIM; see the G9983-MIB)\n        An additional value of none(0) can be returned as a result\n        of a GET operation when a value of the object cannot be\n        determined (for example, a peer GBS cannot be reached), the port\n        does not support any kind of bonding, or when a single-BCE\n        G.998.2 GBS supports bonding (frame fragmentation/reassembly)\n        bypass.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

class IANAgBondScheme(TextualConvention, Integer32):
    description = 'This textual convention defines ITU-T G.998 bonding scheme\n        values.  Possible values are:\n          none(0)    - no bonding (e.g., on a single-BCE G.998.2 GBS)\n                       or unknown\n          g9981(1)   - G.998.1 (G.Bond/ATM)\n          g9982(2)   - G.998.2 (G.Bond/Ethernet)\n          g9983(3)   - G.998.3 (G.Bond/TDIM)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

mibBuilder.exportSymbols("IANA-GBOND-TC-MIB", IANAgBondScheme=IANAgBondScheme, IANAgBondSchemeList=IANAgBondSchemeList, PYSNMP_MODULE_ID=ianaGBondTcMIB, ianaGBondTcMIB=ianaGBondTcMIB)
