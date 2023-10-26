#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.8 at Thu Oct 26 10:05:17 2023
# On host fv-az351-613 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, iso, enterprises, TimeTicks, Gauge32, Bits, MibIdentifier, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "enterprises", "TimeTicks", "Gauge32", "Bits", "MibIdentifier", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, mcafeeGATEWAY=mcafeeGATEWAY, PYSNMP_MODULE_ID=mcafee)
