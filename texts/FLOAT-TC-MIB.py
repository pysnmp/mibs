#
# PySNMP MIB module FLOAT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/FLOAT-TC-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 08:59:04 2024
# On host fv-az1149-759 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Bits, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, mib_2, iso, TimeTicks, MibIdentifier, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "mib-2", "iso", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32")
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

mibBuilder.exportSymbols("FLOAT-TC-MIB", Float32TC=Float32TC, Float64TC=Float64TC, floatTcMIB=floatTcMIB, Float128TC=Float128TC, PYSNMP_MODULE_ID=floatTcMIB)
