#
# PySNMP MIB module RBN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-SMI
# Produced by pysmi-1.1.8 at Thu Oct 12 09:06:41 2023
# On host fv-az245-3 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, ObjectIdentity, MibIdentifier, enterprises, Unsigned32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "enterprises", "Unsigned32", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352))
rbnSMI.setRevisions(('2011-01-19 18:00', '2002-06-06 00:00', '2001-06-27 00:00', '1998-04-18 23:00',))
if mibBuilder.loadTexts: rbnSMI.setLastUpdated('201101191800Z')
if mibBuilder.loadTexts: rbnSMI.setOrganization('Ericsson AB.')
rbnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 1))
if mibBuilder.loadTexts: rbnProducts.setStatus('current')
rbnMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 2))
if mibBuilder.loadTexts: rbnMgmt.setStatus('current')
rbnExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 3))
if mibBuilder.loadTexts: rbnExperiment.setStatus('current')
rbnCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 4))
if mibBuilder.loadTexts: rbnCapabilities.setStatus('current')
rbnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 5))
if mibBuilder.loadTexts: rbnModules.setStatus('current')
rbnEntities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 6))
if mibBuilder.loadTexts: rbnEntities.setStatus('current')
rbnInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 7))
if mibBuilder.loadTexts: rbnInternal.setStatus('current')
mibBuilder.exportSymbols("RBN-SMI", PYSNMP_MODULE_ID=rbnSMI, rbnEntities=rbnEntities, rbnProducts=rbnProducts, rbnCapabilities=rbnCapabilities, rbnExperiment=rbnExperiment, rbnSMI=rbnSMI, rbnMgmt=rbnMgmt, rbnModules=rbnModules, rbnInternal=rbnInternal)
