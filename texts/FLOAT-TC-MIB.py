#
# PySNMP MIB module FLOAT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/FLOAT-TC-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:55:06 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Counter64, Bits, mib_2, ObjectIdentity, Gauge32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "mib-2", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
floatTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 201))
floatTcMIB.setRevisions(('2011-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: floatTcMIB.setRevisionsDescriptions(('Initial version, published as RFC 6340.',))
if mibBuilder.loadTexts: floatTcMIB.setLastUpdated('201107270000Z')
if mibBuilder.loadTexts: floatTcMIB.setOrganization('IETF OPSAWG Working Group')
if mibBuilder.loadTexts: floatTcMIB.setContactInfo('WG Email: opsawg@ietf.org\n\n                  Editor: Randy Presuhn\n                  randy_presuhn@mindspring.com')
if mibBuilder.loadTexts: floatTcMIB.setDescription("Textual conventions for the representation\n                  of floating-point numbers.\n\n                  Copyright (c) 2011 IETF Trust and the persons\n                  identified as authors of the code.  All rights\n                  reserved.\n\n                  Redistribution and use in source and binary forms,\n                  with or without modification, is permitted pursuant\n                  to, and subject to the license terms contained in,\n                  the Simplified BSD License set forth in Section\n                  4.c of the IETF Trust's Legal Provisions Relating\n                  to IETF Documents\n                  (http://trustee.ietf.org/license-info).\n\n                  This version of this MIB module is part of RFC 6340;\n                  see the RFC itself for full legal notices.")
class Float32TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic,\n                  Standard 754-2008'
    description = 'This type represents a 32-bit (4-octet) IEEE\n                  floating-point number in binary interchange format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class Float64TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic,\n                  Standard 754-2008'
    description = 'This type represents a 64-bit (8-octet) IEEE\n                  floating-point number in binary interchange format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Float128TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic,\n                  Standard 754-2008'
    description = 'This type represents a 128-bit (16-octet) IEEE\n                  floating-point number in binary interchange format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

mibBuilder.exportSymbols("FLOAT-TC-MIB", Float32TC=Float32TC, PYSNMP_MODULE_ID=floatTcMIB, Float64TC=Float64TC, floatTcMIB=floatTcMIB, Float128TC=Float128TC)
