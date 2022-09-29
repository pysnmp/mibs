#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.8 at Thu Sep 29 13:18:07 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, enterprises, NotificationType, Counter64, Gauge32, Integer32, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "NotificationType", "Counter64", "Gauge32", "Integer32", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rittal = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606))
rittal.setRevisions(('2011-04-01 00:00',))
if mibBuilder.loadTexts: rittal.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: rittal.setOrganization('RITTAL GmbH & Co. KG')
mibBuilder.exportSymbols("RITTAL-SMI-MIB", PYSNMP_MODULE_ID=rittal, rittal=rittal)
