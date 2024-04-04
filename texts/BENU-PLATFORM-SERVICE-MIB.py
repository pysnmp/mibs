#
# PySNMP MIB module BENU-PLATFORM-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-SERVICE-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:47:15 2024
# On host fv-az1490-927 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, IpAddress, Gauge32, Unsigned32, Counter32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "IpAddress", "Gauge32", "Unsigned32", "Counter32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatSerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2))
benuPlatSerMIB.setRevisions(('2012-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuPlatSerMIB.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuPlatSerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: benuPlatSerMIB.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuPlatSerMIB.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benuPlatSerMIB.setDescription('The MIB module defines all platform services\n                mibs that are specific to benu enterprise\n\n                Copyright (C)  2012 by Benu Networks, Inc.\n                All rights reserved.')
mibBuilder.exportSymbols("BENU-PLATFORM-SERVICE-MIB", PYSNMP_MODULE_ID=benuPlatSerMIB, benuPlatSerMIB=benuPlatSerMIB)
