#
# PySNMP MIB module BENU-PLATFORM-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-SERVICE-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 14:10:58 2023
# On host fv-az613-163 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, MibIdentifier, ModuleIdentity, ObjectIdentity, Bits, iso, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Bits", "iso", "Unsigned32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatSerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2))
benuPlatSerMIB.setRevisions(('2012-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuPlatSerMIB.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuPlatSerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: benuPlatSerMIB.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuPlatSerMIB.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benuPlatSerMIB.setDescription('The MIB module defines all platform services\n                mibs that are specific to benu enterprise\n\n                Copyright (C)  2012 by Benu Networks, Inc.\n                All rights reserved.')
mibBuilder.exportSymbols("BENU-PLATFORM-SERVICE-MIB", benuPlatSerMIB=benuPlatSerMIB, PYSNMP_MODULE_ID=benuPlatSerMIB)
